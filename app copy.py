from flask import Flask, request, jsonify
import numpy as np
import pickle
import joblib

RFC_MODEL = joblib.load("models/sleep_disorder_rfc_model.pkl")
SCLAER_MODEL = joblib.load("models/SCALER_MODEL.pkl")

def return_prediction(model, scaler, sample_json):
    a = list(sample_json.values())
    a = [float(i) for i in a]
    data = SCLAER_MODEL.transform([a])
    result = RFC_MODEL.predict(data)
    labels = ["Insomnia", "None", "Sleep Apnea"]
    predicted_class = labels[result[0]]
    return predicted_class

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>FLASK APP IS RUNNING!</h1>'

@app.route('/prediction', methods=['POST'])
def predict_sleep_disorder():
    # RECEIVE THE REQUEST
    content = request.json

    # PRINT THE DATA PRESENT IN THE REQUEST
    print("[INFO] Request: ", content)

    # PREDICT THE CLASS USING HELPER FUNCTION
    prediction_result = return_prediction(model=RFC_MODEL, scaler=SCLAER_MODEL, sample_json=content)

    # ADD THE PREDICTION RESULT TO THE INPUT DATA
    content['sleep_disorder'] = prediction_result

    # PRINT THE RESULT
    print("[INFO] Response: ", prediction_result)

    # SEND THE RESULT AS JSON OBJECT
    return jsonify(prediction_result)

if __name__ == '__main__':
    app.run("0.0.0.0")
