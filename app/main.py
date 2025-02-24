from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # 1 load the image 
    # 2 image to tensor 
    # 3 prediction 
    # 4 return prediction json
    return jsonify ({'result': 1})