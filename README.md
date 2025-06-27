# 📊 Insight Engine: AI-Powered Chart Recommender

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![Framework: FastAPI](https://img.shields.io/badge/Framework-FastAPI-green.svg)

Insight Engine is a sophisticated full-stack web application designed to bridge the gap between raw data and actionable insights. By leveraging the power of Google's Gemini AI, this tool intelligently analyzes uploaded CSV or XLSX files and automatically recommends the most effective and relevant data visualizations.

This project serves as a comprehensive demonstration of modern web development practices, featuring a decoupled frontend, a high-performance RESTful API backend, and seamless integration with a third-party AI service.

---

## ✨ Key Features

-   **🤖 AI-Powered Analysis:** Utilizes Google Gemini to understand the context and structure of your data, providing intelligent chart suggestions.
-   **📁 Versatile File Support:** Accepts both common data formats: `.csv` and `.xlsx`.
-   **🎨 Elegant & Responsive UI:** A clean, professional, and mobile-friendly single-page interface built with modern HTML, CSS, and JavaScript.
-   **💡 Intuitive User Experience:** Features include drag-and-drop file uploads, a "file pill" preview, and a shimmering skeleton loader to provide clear feedback during processing.
-   **⚙️ High-Performance Backend:** Built with FastAPI, one of the fastest Python web frameworks available, ensuring snappy response times.
-   **🏗️ Decoupled Architecture:** A robust separation between the frontend and backend allows for independent development, scaling, and maintenance.

---

## 📂 Project Structure

The project is organized into a clean, decoupled `backend` and `frontend` structure.
AI-Chart-Recommender/
│
├── .gitignore # Specifies intentionally untracked files to ignore
├── backend/
│ ├── .env # (To be created) Holds the secret API key
│ ├── main.py # The main FastAPI application logic
│ └── venv/ # (To be created) The isolated Python virtual environment
│
├── frontend/
│ ├── index.html # The single HTML file for the user interface
│ ├── script.js # JavaScript for interactivity and API calls
│ └── style.css # All CSS styles for the application
│
├── LICENSE # The project's open-source license
├── README.md # You are here!
└── requirements.txt # A list of all Python dependencies for the backend
## 🛠️ Tech Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend** | **Python** | Core programming language |
| | **FastAPI** | High-performance web framework for the API |
| | **Pandas** | Data analysis and manipulation |
| | **Matplotlib** | Generating static chart images |
| | **Openpyxl** | Engine for reading `.xlsx` files |
| | **Uvicorn** | ASGI server to run FastAPI |
| | **Google Generative AI**| The LLM for chart recommendations |
| **Frontend** | **HTML5, CSS3, JavaScript**| Structure, styling, and interactivity |

---

## 🚀 Getting Started & Installation

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

-   [Python](https://www.python.org/downloads/) (version 3.10 or newer)
-   [Git](https://git-scm.com/downloads/)
-   A **Google Gemini API Key** from the [Google AI Studio](https://aistudio.google.com/app/apikey).
-   [Visual Studio Code](https://code.visualstudio.com/) with the **Live Server** extension.

### Full Setup Guide

**Step 1: Clone the Repository**

Open your terminal and clone the repository to your local machine.

```bash
git clone https://github.com/Suyashthakur08/AI-Chart-Recommender.git
cd AI-Chart-Recommender
Step 2: Set Up the Backend Virtual Environment
This step creates an isolated environment for the backend's Python dependencies, which is a critical best practice
# From the project's root directory, navigate into the backend folder
cd backend

# Create a Python virtual environment (named 'venv' for example)
python -m venv venv

# Activate the newly created environment
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# On macOS/Linux:
source venv/bin/activate
Step 3: Install Backend Dependencies
With the virtual environment active, install all the required Python packages from the requirements.txt file
pip install -r ../requirements.txt
Step 4: Configure Your API Key
Your secret API key must be stored securely in an environment variable file.
While still in the backend directory, create a new file named .env.
Open this .env file and add your Gemini API key in this exact format:
GEMINI_API_KEY="YOUR_SECRET_API_KEY_HERE"
🏃‍♂️ Running the Application
To see the application in action, you must run both the backend and frontend servers simultaneously in two separate terminals.
Terminal 1: Start the Backend Server
Open your first terminal.
Navigate to the backend directory.
Ensure your virtual environment is activated (you should see (venv) in your prompt).
Start the FastAPI server with Uvicorn:
uvicorn main:app --reload
The backend is now live and listening at http://127.0.0.1:8000. Keep this terminal running.
Terminal 2: Start the Frontend Server
Open a new, second terminal or use the VS Code interface.
Make sure your VS Code is open to the project's root folder (AI-Chart-Recommender).
In the VS Code file explorer on the left, navigate into the frontend folder.
Right-click on index.html and select "Open with Live Server".
Your browser will automatically open the application, usually at a URL like http://127.0.0.1:5500.
You can now upload a CSV or XLSX file and see the Insight Engine work!
📄 License
This project is licensed under the MIT License. See the LICENSE file for details.