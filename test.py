from flask import Flask, request, render_template
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    loaded_scaler = pickle.load(file)

@app.route('/')
def index():
    return render_template("index.html", prediction=None, error=None)

@app.route('/predict', methods=['POST'])
def predict_risk():
    try:
        data = request.form

        processed_data = [
            int(data['Age']),
            int(data['SystolicBP']),
            int(data['DiastolicBP']),
            float(data['BS']),
            float(data['BodyTemp']),
            int(data['HeartRate'])
        ]

        processed_data = loaded_scaler.transform([processed_data])[0]
        prediction = model.predict([processed_data])

        if prediction[0] == 1:
            prediction = "Medium Risk"
        elif prediction[0] == 2:
            prediction = "High Risk"
        elif prediction[0] == 0:
            prediction = "Low Risk"
        else:
            prediction = "Unknown Risk Level"

        return render_template("index.html", prediction=prediction, error=None)

    except Exception as e:
        print("Error during prediction:", e)
        return render_template("index.html", prediction=None, error=str(e))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
