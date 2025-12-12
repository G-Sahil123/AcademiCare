# 🎓 Student Dropout Prediction System with AI Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)]
[![Streamlit](https://img.shields.io/badge/streamlit-app-orange.svg)]

> End-to-end ML web app that predicts student dropout risk and provides an integrated AI assistant for insights and explanations.

---

## 🚀 Project Overview

This repository contains a Streamlit application that:
- Predicts student dropout probability using a trained ML model.
- Provides an integrated AI Assistant (Groq) to explain predictions and suggest interventions.
- Includes data preprocessing, feature engineering, model training and a simple UI.

---

## 🔧 Features

- Dropout risk prediction (classification)
- Preprocessing and feature engineering 
- Model training & evaluation (supports saving/loading models)
- Streamlit web UI with:
  - Prediction page
  - AI Assistant chat page
- Secrets management using `.streamlit/secrets.toml`
- Example notebooks / scripts for experiments


---

## ⚙️ Installation & Local Setup

**1. Clone the repo**
```bash
git clone https://github.com/your-username/student_dropout_prediction_app.git
cd student_dropout_prediction_app
```
**2. Create the virtual environment**
```bash
python -m venv stuenv

# Windows
stuenv\Scripts\activate

# macOS / Linux
source stuenv/bin/activate
```
**3. Install dependencies**
```bash
pip install -r requirements.txt
```
4. Create the .streamlit folder and secrets.toml (do NOT commit this file):
```bash
mkdir .streamlit


Create .streamlit/secrets.toml with:

# .streamlit/secrets.toml
GROQ_API_KEY = "sk-REPLACE_WITH_YOUR_KEY"
# Add any other secrets your app expects:
# DB_URL = "..."
# OTHER_API_KEY = "..."
```
**5. Run the app**
```bash
streamlit run app.py
```
