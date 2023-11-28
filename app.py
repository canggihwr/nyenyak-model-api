from flask import Flask, request, jsonify
import json
import numpy as np
import pickle
import joblib

RFC_MODEL = joblib.load("models/sleep_disorder_rfc_model.pkl")

def return_prediction(model, sample_json):
    predictions = []

    if isinstance(sample_json, dict):
        data = [list(sample_json.values())]
        result = model.predict(data)
        labels = ["Insomnia", "None", "Sleep Apnea"]
        predicted_class = labels[result[0]]
        predictions.append(predicted_class)
    else:
        print("[ERROR] Invalid JSON format. Expected a dictionary.")

    return predictions

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>FLASK APP IS RUNNING!</h1>'

@app.route('/prediction', methods=['POST'])
def predict_sleep_disorder():
    # RECEIVE THE REQUEST
    content = request.get_json(force=True)  # Parse JSON

    # PREDICT THE CLASS USING HELPER FUNCTION
    prediction_result = return_prediction(model=RFC_MODEL, sample_json=content)

    # ADD THE PREDICTION RESULT TO THE INPUT DATA
    content['sleep_disorder'] = prediction_result

    # PRINT THE RESULT
    print("[INFO] Response: ", prediction_result)

    # SEND THE RESULT AS JSON OBJECT
    return jsonify(prediction_result)

if __name__ == '__main__':
    app.run("0.0.0.0")
