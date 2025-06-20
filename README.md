# Rainfall-Prediction
Our ML model on Rainfall Prediction

Overview:
This is a machine learning-based web app that predicts whether it will rain tomorrow based on weather parameters like temperature, humidity, pressure, wind speed, and direction. It uses a trained model to provide binary predictions (Rain / No Rain).

How It Works:
Users enter weather data via a web form.

Data is processed using an imputer and scaler.

A trained model (rainfall.pkl) predicts rainfall.

Output is shown through rain.html or noRain.html.

Tech Stack
Backend: Flask (Python)

Frontend: HTML/CSS

ML: Scikit-learn (imputer, scaler, classifier)

Run Locally
bash
Copy
Edit
pip install flask pandas numpy scikit-learn
python app.py
Open the displayed url locally in your pc 

Files
app.py – Main application

rainfall.pkl – Trained model

scale.pkl – Feature scaler

impter.pkl – Categorical imputer

HTML files – UI for input and results



