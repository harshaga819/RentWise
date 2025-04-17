from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load all .pkl files
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
locations = pickle.load(open("location.pkl", "rb"))
feature_columns = pickle.load(open("feature_columns.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html', locations=locations, show_form=False)

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from form
    location = request.form['location']
    bhk = int(request.form['bhk'])
    area = float(request.form['area'])
    price_per_sqft = float(request.form['price_per_sqft'])

    # Step 1: Scale the Carpet Area
    area_scaled = scaler.transform([[area]])[0][0]

    # Step 2: Initialize input dictionary with all required features
    input_dict = {
        'Carpet Area': area_scaled,
        'BHK': bhk,
        'Price_per_sqft': price_per_sqft
    }

    # Step 3: One-hot encode location manually
    for loc in locations:
        col_name = f"Location_{loc}"
        input_dict[col_name] = 1 if loc == location else 0

    # Step 4: Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Step 5: Align with feature columns (fill missing with 0)
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    # Step 6: Predict
    predicted_rent = model.predict(input_df)[0]

    # Step 7: Return prediction
    return render_template('index.html', prediction=round(predicted_rent, 3), locations=locations, show_form=True)

if __name__ == "__main__":
    app.run(debug=True)
