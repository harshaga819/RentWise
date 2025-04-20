from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
locations = pickle.load(open("location.pkl", "rb"))
feature_columns = pickle.load(open("feature_columns.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html', locations=locations, show_form=False)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        location = request.form['location']
        bhk = int(request.form['bhk'])
        area = float(request.form['area'])
        price_per_sqft = float(request.form['price_per_sqft'])

        # Scale the Carpet Area
        area_scaled = scaler.transform([[area]])[0][0]

        # Initialize input dictionary with all required features
        input_dict = {
            'Carpet Area': area_scaled,
            'BHK': bhk,
            'Price_per_sqft': price_per_sqft
        }

        # One-hot encode location manually
        for loc in locations:
            col_name = f"Location_{loc}"
            input_dict[col_name] = 1 if loc == location else 0

        # Convert to DataFrame
        input_df = pd.DataFrame([input_dict])

        # Align with feature columns (fill missing with 0)
        input_df = input_df.reindex(columns=feature_columns, fill_value=0)

        # Predict
        predicted_rent = model.predict(input_df)[0]

        # Calculate rent range
        rent_range_lower = predicted_rent * 0.9
        rent_range_upper = predicted_rent * 1.1 

        # Convert the numpy float32 to a native Python float to ensure it's JSON serializable
        return jsonify({
            'prediction_range': f"₹{round(rent_range_lower, 2)} - ₹{round(rent_range_upper, 2)}"
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
