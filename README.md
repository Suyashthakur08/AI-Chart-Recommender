# 📊 Insight Engine: AI-Powered Chart Recommender

Insight Engine is a modern, full-stack web application that uses AI to automatically recommend the most suitable charts for any uploaded dataset. It supports both CSV and Excel files and delivers intelligent visualization suggestions using Google Gemini.

The app features a clean and responsive frontend, a high-performance FastAPI backend, and seamless integration with a generative AI model.

---

## ✨ Features

- **AI-Powered Analysis**: Uses Google Gemini to understand your data and recommend charts.
- **CSV/XLSX File Support**: Upload common data formats directly.
- **User-Friendly UI**: Clean drag-and-drop interface, real-time feedback, and file preview.
- **FastAPI Backend**: High-speed REST API architecture.
- **Fully Decoupled Frontend/Backend**: Easier to maintain, scale, and extend.

---

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI, Pandas, Matplotlib, Openpyxl, Uvicorn
- **AI Integration**: Google Generative AI (Gemini)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)

---

## 📁 Project Overview

- `backend/` — FastAPI application backend
  - `main.py` — API logic and routes
  - `.env` — Stores your Gemini API key (not included in source control)
- `frontend/` — Frontend UI
  - `index.html` — Main web page
  - `style.css` — Styling for UI
  - `script.js` — JavaScript for interactivity and API requests
- `requirements.txt` — Python package dependencies
- `README.md` — Project documentation
- `LICENSE` — MIT License
- `.gitignore` — Excludes `venv`, `.env`, and other unnecessary files

---

## ✅ Prerequisites

- Python 3.10 or newer
- Git
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
- Visual Studio Code (optional, for Live Server extension)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Suyashthakur08/AI-Chart-Recommender.git
cd AI-Chart-Recommender
```

### 2. Set Up the Backend

```bash
cd backend
python -m venv venv
```

Activate the virtual environment:
On Windows:
```bash
.\venv\Scripts\Activate.ps1
```

On macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r ../requirements.txt
```

### 4. Add Your Gemini API Key
Create a .env file inside the backend/ directory and add the following:

```
GEMINI_API_KEY="your_google_gemini_api_key_here"
```

## 🧪 Running the Application

### Start Backend (Terminal 1)
Make sure you're inside the backend/ directory with the virtual environment activated:

```bash
uvicorn main:app --reload
```

This starts the FastAPI server at ```http://127.0.0.1:8000```.

### Start Frontend (Terminal 2)
Use Live Server (or any static server) to open ```frontend/index.html```, or open it directly in a browser.

If using Live Server in VS Code, the app will open at ```http://127.0.0.1:5500```.

## 🧠 How It Works
Upload a ```.csv``` or ```.xlsx``` file via the web interface.

The frontend sends your data to the backend.

FastAPI reads the file, processes it using Pandas, and sends metadata to Gemini.

Gemini analyzes the data and suggests appropriate chart types.

The chart is rendered and displayed back in the UI.
