# Rainfall-Prediction
Our ML model on Rainfall Prediction

🌧️ Rainfall Prediction System
📌 Project Overview:
This project is a Machine Learning-powered web application that predicts whether it will rain tomorrow based on various weather parameters. The system is built using Python (Flask) on the backend and provides a user-friendly web interface to collect weather input and display predictions.

🤖 Model Description:
The ML model behind this system is trained to classify whether rainfall will occur the next day. It uses various features like temperature, humidity, wind speed/direction, and atmospheric pressure. The trained model is stored in rainfall.pkl.

🔍 Key Features Used:
Location
Temperature: MinTemp, MaxTemp, Temp9am, Temp3pm
Humidity: Humidity9am, Humidity3pm
Pressure: Pressure9am, Pressure3pm
Rainfall (current day)
Wind Info: WindGustSpeed, WindSpeed9am, WindSpeed3pm, Wind directions
RainToday: Whether it rained today
Month: Automatically extracted from the date

🧠 ML Pipeline Components:
Imputer (impter.pkl) to handle missing categorical values
Scaler (scale.pkl) for feature normalization
Classifier Model (rainfall.pkl) — trained binary classification model

🖥️ Application Workflow:
User Input: User enters weather data through an intuitive HTML form (index.html).

Preprocessing:
Missing values in categorical inputs are imputed.
One-hot encoding is applied.
Data is scaled using the trained scaler.

Prediction:
The preprocessed input is passed to the trained model.
The model predicts 1 for rain and 0 for no rain.

Output:
If rain is predicted, rain.html is rendered.
Otherwise, noRain.html is displayed.
exit.html is used as a thank-you or goodbye page.

🚀 How to Run the App:
Install Requirements:
bash
Copy
Edit
pip install flask pandas numpy scikit-learn

Run the App:
bash
Copy
Edit
python app.py
Open in Browser:
Visit http://127.0.0.1:5000 to access the prediction system.

📁 File Structure
php
Copy
Edit
├── app.py              # Flask backend
├── rainfall.pkl        # Trained ML model
├── scale.pkl           # Feature scaler
├── impter.pkl          # Imputer for categorical data
├── index.html          # Main input form
├── rain.html           # Page shown if rain is predicted
├── noRain.html         # Page shown if no rain is predicted
├── exit.html           # Exit/Thank-you page

📌 Use Cases
-Personal weather planning
-Agriculture and irrigation forecasting
-Event scheduling in outdoor conditions

