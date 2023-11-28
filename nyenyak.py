from flask import Flask, request, jsonify
from joblib import load
import numpy as np
import requests

app = Flask(__name__)

# Load the saved model
loaded_model = load("models/sleep_disorder_rfc_model.pkl")

@app.route('/')
def index():
    return '<h1>FLASK APP IS RUNNING!</h1>'

@app.route('/prediction', methods=['POST'])
def predict_sleep_disorder():
    # RECEIVE THE REQUEST
    content = request.json

    # PRINT THE DATA IN THE REQUEST
    print("[INFO] Request: ", content)

    # CONVERT INPUT TO NUMPY ARRAY
    input_data = np.array(list(content.values())).reshape(1, -1)

    # PREDICT THE CLASS USING THE LOADED MODEL
    result = loaded_model.predict(input_data)
    labels = ["Insomnia", "None", "Sleep Apnea"]
    predicted_class = labels[result[0]]

    # ADD THE PREDICTION RESULT TO THE INPUT DATA
    content['sleep_disorder'] = predicted_class

    # PRINT THE RESULT
    print("[INFO] Response: ", predicted_class)

    # SEND THE RESULT AS JSON OBJECT
    return jsonify(content)

if __name__ == '__main__':
    app.run("0.0.0.0")