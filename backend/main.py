# backend/main.py (Final Stable Version)

import pandas as pd
import matplotlib.pyplot as plt
import google.generativeai as genai
import json
import re
import os
from dotenv import load_dotenv

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import io
import base64

# --- CONFIG ---
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# --- Initialize FastAPI App ---
app = FastAPI(
    title="AI Chart Recommender API",
    description="Upload a CSV or XLSX file, get back AI-recommended chart images."
)

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- DATA PROCESSING LOGIC ---

def summarize_dataframe(df: pd.DataFrame, max_columns=10) -> str:
    summary = []
    for col in df.columns[:max_columns]:
        dtype = str(df[col].dtype)
        nunique = df[col].nunique()
        sample = df[col].dropna().unique()[:3]
        summary.append(f"- {col}: {dtype}, {nunique} unique values, sample: {list(sample)}")
    return "\n".join(summary)

def ask_gemini_for_charts(summary: str) -> list:
    prompt = f"""
You are a chart recommendation assistant.

Based on this dataset summary:
{summary}

Return a JSON array of chart recommendations. Each item should follow:
{{
  "chart_type": "bar" | "line" | "scatter" | "histogram" | "pie",
  "x_column": "column_name",
  "y_column": "column_name" (optional for histogram and pie),
  "title": "chart title"
}}

Return only valid JSON. No explanation or markdown.
"""
    try:
        response = model.generate_content(prompt)
        content = response.text.strip()
        content = re.sub(r"^```json\s*", "", content)
        content = re.sub(r"\s*```$", "", content)
        charts = json.loads(content)
        return charts if isinstance(charts, list) else []
    except Exception as e:
        print(f"Error parsing Gemini response: {e}")
        return []

def create_chart_base64(df: pd.DataFrame, config: dict):
    chart_type = config.get("chart_type")
    x_col = config.get("x_column")
    y_col = config.get("y_column")
    title = config.get("title", "Untitled Chart")
    
    if x_col not in df.columns or (y_col and y_col not in df.columns):
        return None

    fig, ax = plt.subplots(figsize=(8, 5))
    
    try:
        if chart_type == "bar":
            if y_col and pd.api.types.is_numeric_dtype(df[y_col]):
                df.groupby(x_col)[y_col].mean().plot(kind="bar", ax=ax)
            else:
                df[x_col].value_counts().plot(kind="bar", ax=ax)
        elif chart_type == "line":
            df.plot(x=x_col, y=y_col, kind="line", ax=ax)
        elif chart_type == "scatter":
            ax.scatter(df[x_col], df[y_col])
        elif chart_type == "histogram":
            df[x_col].plot(kind="hist", bins=20, ax=ax)
        elif chart_type == "pie":
            data = df[x_col].value_counts()
            data.plot(kind="pie", autopct='%1.1f%%', ax=ax, startangle=90)
            ax.set_ylabel("")
        else:
            plt.close(fig)
            return None
        
        ax.set_title(title, fontsize=14)
        if chart_type != "pie":
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col if y_col else "Frequency")
        
        plt.tight_layout()
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        plt.close(fig)
        buf.seek(0)
        img_str = base64.b64encode(buf.read()).decode('utf-8')
        return img_str

    except Exception as e:
        print(f"Error creating chart '{title}': {e}")
        plt.close(fig)
        return None

# --- API ENDPOINT ---
@app.post("/analyze/")
async def analyze_file(file: UploadFile = File(...)):
    filename = file.filename
    if not (filename.endswith('.csv') or filename.endswith('.xlsx')):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV or XLSX file.")
    
    try:
        content = await file.read()

        if filename.endswith('.csv'):
            df = pd.read_csv(io.StringIO(content.decode('utf-8')))
        elif filename.endswith('.xlsx'):
            df = pd.read_excel(io.BytesIO(content))

        summary = summarize_dataframe(df)
        chart_configs = ask_gemini_for_charts(summary)

        if not chart_configs:
            return {"message": "AI could not generate chart recommendations for this dataset."}

        results = []
        for config in chart_configs:
            img_base64 = create_chart_base64(df, config)
            if img_base64:
                results.append({
                    "title": config.get("title", "Untitled Chart"),
                    "image_base64": img_base64
                })

        return {"charts": results}

    except Exception as e:
        print(f"Error during file processing: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the file: {e}")