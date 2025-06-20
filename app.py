import numpy as np
import pickle
import pandas as pd
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='.')

# Load objects
model = pickle.load(open("rainfall.pkl", "rb"))
scaler = pickle.load(open("scale.pkl", "rb"))
imputer = pickle.load(open("impter.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/exit')
def exit_page():
    return render_template("exit.html")

@app.route('/predict', methods=["POST"])
def predict():
    try:
        # Get the feature names that the scaler was trained on
        trained_columns = scaler.feature_names_in_
        
        # Collect all form data
        data_dict = {
            'Location': request.form.get("location"),
            'MinTemp': float(request.form.get("minTemp")),
            'MaxTemp': float(request.form.get("maxTemp")),
            'Rainfall': float(request.form.get("rainfall")),
            'WindGustSpeed': float(request.form.get("windGustSpeed")),
            'WindSpeed9am': float(request.form.get("windSpeed9am")),
            'WindSpeed3pm': float(request.form.get("windSpeed3pm")),
            'Humidity9am': float(request.form.get("humidity9am")),
            'Humidity3pm': float(request.form.get("humidity3pm")),
            'Pressure9am': float(request.form.get("pressure9am")),
            'Pressure3pm': float(request.form.get("pressure3pm")),
            'Temp9am': float(request.form.get("temp9am")),
            'Temp3pm': float(request.form.get("temp3pm")),
            'Month': int(request.form.get("month")),
            # Categorical features from the form
            'RainToday': request.form.get("rainToday"),
            'WindGustDir': request.form.get("windGustDir"),
            'WindDir9am': request.form.get("windDir9am"),
            'WindDir3pm': request.form.get("windDir3pm")
        }

        # Create DataFrame
        df = pd.DataFrame([data_dict])
        
        # Separate categorical columns that need imputation
        cat_columns = ['RainToday', 'WindGustDir', 'WindDir9am', 'WindDir3pm']
        data_cat = df[cat_columns]
        
        # Apply the imputer to categorical data
        data_cat_imputed = imputer.transform(data_cat)
        data_cat_imputed_df = pd.DataFrame(data_cat_imputed, columns=cat_columns)
        
        # Remove original categorical columns and add imputed ones
        df_processed = df.drop(columns=cat_columns)
        df_processed = pd.concat([df_processed, data_cat_imputed_df], axis=1)
        
        # Apply one-hot encoding (same as training)
        df_encoded = pd.get_dummies(df_processed, drop_first=True)
        
        # Ensure all columns match the training data
        # Add missing columns with 0 values
        for col in trained_columns:
            if col not in df_encoded.columns:
                df_encoded[col] = 0
        
        # Remove extra columns that weren't in training
        df_encoded = df_encoded[trained_columns]
        
        # Convert to numeric and handle any remaining issues
        df_encoded = df_encoded.apply(pd.to_numeric, errors='coerce')
        df_encoded = df_encoded.fillna(0)
        df_encoded = df_encoded.astype(np.float64)
        
        # Scale the features
        df_scaled = scaler.transform(df_encoded)
        
        # Make prediction
        prediction = model.predict(df_scaled)[0]
        
        if prediction == 1:  # Note: model returns 0/1, not "Yes"/"No"
            return render_template("rain.html")
        else:
            return render_template("noRain.html")
        
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)