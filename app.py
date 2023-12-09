import os
from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load the saved model in .h5 format
loaded_model = tf.keras.models.load_model("models/model_ann.h5")

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
    
    # Assuming the result is a probability distribution over classes
    predicted_class_index = np.argmax(result)
    labels = ["Insomnia", "None", "Sleep Apnea"]
    predicted_class = labels[predicted_class_index]

    # ADD THE PREDICTION RESULT TO THE INPUT DATA
    content['sleep_disorder'] = predicted_class

    # PRINT THE RESULT
    print("[INFO] Response: ", predicted_class)

    # SEND THE RESULT AS JSON OBJECT
    return jsonify(content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
