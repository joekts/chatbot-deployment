#Import modules
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

#Setup the flask app, with CORS to enable the standalone frontend
app = Flask(__name__)
CORS(app)

#Creating the post request
@app.post("/predict")
def predict():
    text = request.get_json().get("message")

    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)