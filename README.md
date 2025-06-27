# 📊 Insight Engine: AI-Powered Chart Recommender

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![Framework: FastAPI](https://img.shields.io/badge/Framework-FastAPI-green.svg)

Insight Engine is a sophisticated full-stack web application designed to bridge the gap between raw data and actionable insights. By leveraging the power of Google's Gemini AI, this tool intelligently analyzes uploaded CSV or XLSX files and automatically recommends the most effective and relevant data visualizations.

This project serves as a comprehensive demonstration of modern web development practices, featuring a decoupled frontend, a high-performance RESTful API backend, and seamless integration with a third-party AI service.

---

## 📸 Application Preview

*(**Action Required:** It is highly recommended to add a GIF of your app in action here. It makes a huge difference! Use a free tool like Giphy Capture or ScreenToGif to record your screen and drag the saved GIF file into this editor.)*

<p align="center">
  <!-- ADD YOUR SCREENSHOT OR GIF HERE -->
</p>

---

## ✨ Key Features

-   **🤖 AI-Powered Analysis:** Utilizes Google Gemini to understand the context and structure of your data, providing intelligent chart suggestions.
-   **📁 Versatile File Support:** Accepts both common data formats: `.csv` and `.xlsx`.
-   **🎨 Elegant & Responsive UI:** A clean, professional, and mobile-friendly single-page interface built with modern HTML, CSS, and JavaScript.
-   **💡 Intuitive User Experience:** Features include drag-and-drop file uploads, a "file pill" preview, and a shimmering skeleton loader to provide clear feedback during processing.
-   **⚙️ High-Performance Backend:** Built with FastAPI, one of the fastest Python web frameworks available, ensuring snappy response times.
-   **🏗️ Decoupled Architecture:** A robust separation between the frontend and backend allows for independent development, scaling, and maintenance.

---

## 🏛️ Project Architecture

The application follows a standard client-server model:

<p align="center">
  <pre>
  +-----------------+      HTTP Request      +----------------+      API Call       +-------------------+
  |                 |  (File, /analyze/)   |                |  (Data Summary)  |                   |
  | Frontend (User) |--------------------> |  Backend API   |------------------>|  Google Gemini AI |
  | (Browser)       |                      | (FastAPI)      |                  |     (LLM)         |
  |                 |  <--------------------|                | <------------------|                   |
  |                 |   (JSON with Charts) |                |   (JSON with      |                   |
  +-----------------+      HTTP Response     +----------------+   Recommendations) +-------------------+
  </pre>
</p>

1.  The **Frontend** captures the user's file upload.
2.  It sends the file to the `/analyze/` endpoint on the **Backend API**.
3.  The **Backend** reads the file with Pandas, creates a concise summary, and sends this summary to the **Google Gemini API**.
4.  Gemini returns a structured JSON list of chart recommendations.
5.  The backend uses Matplotlib to generate a PNG image for each recommendation, encodes it to Base64, and sends the complete data back to the frontend.
6.  The frontend dynamically renders the results for the user.

---

## 🛠️ Tech Stack

### Backend
| Technology | Purpose |
| :--- | :--- |
| **Python** | Core programming language |
| **FastAPI** | High-performance web framework for the API |
| **Pandas** | Data analysis and manipulation |
| **Matplotlib** | Generating static chart images |
| **Openpyxl** | Engine for reading `.xlsx` files |
| **Uvicorn** | ASGI server to run FastAPI |
| **Google Generative AI**| The LLM for chart recommendations |
| **python-dotenv** | Managing environment variables |

### Frontend
| Technology | Purpose |
| :--- | :--- |
| **HTML5** | Content structure |
| **CSS3** | Styling, layout, and animations (Flexbox, Grid, Custom Properties) |
| **Vanilla JavaScript** | DOM manipulation, user interaction, and API communication (Fetch API)|

---

## 🚀 Getting Started

Follow these instructions to set up and run the project on your local machine for development and testing purposes.

### Prerequisites

-   [Python](https://www.python.org/downloads/) (version 3.10 or newer)
-   [Git](https://git-scm.com/downloads/)
-   A **Google Gemini API Key** from the [Google AI Studio](https://aistudio.google.com/app/apikey).
-   [Visual Studio Code](https://code.visualstudio.com/) with the **Live Server** extension.

### Installation & Setup

**1. Clone the Repository:**

```bash
git clone https://github.com/Suyashthakur08/AI-Chart-Recommender.git
cd AI-Chart-Recommender