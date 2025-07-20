
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open("model/heart_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    features = [float(x) for x in request.form.values()]
    final_input = np.array([features])
    result = model.predict(final_input)[0]
    return render_template("index.html", prediction_text="Predicted Outcome: {}".format("Death" if result else "Survival"))

if __name__ == "__main__":
    app.run(debug=True)
