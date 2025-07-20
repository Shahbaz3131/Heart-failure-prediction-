# Heart-failure-prediction-
This project predicts the likelihood of heart failure based on patient health records using a trained Random Forest Classifier. It includes a Flask backend and a custom HTML form for user interaction.

🔗 Live Demo
✅ [Add your Render app link here]
Example: https://heart-failure-predictor.onrender.com

📊 Dataset
Source: Heart Failure Clinical Dataset – Kaggle
Rows: 299 | Features: 13
Target variable: DEATH_EVENT (1 = Death, 0 = Survived)

🚀 Features
Train & evaluate model using Random Forest
Flask web app for real-time prediction
Clean and responsive HTML form with custom CSS
Render deployment-ready

📦 Tech Stack
Frontend: HTML, CSS
Backend: Flask (Python)
ML Libraries: pandas, scikit-learn, numpy
Model: Random Forest Classifier (~83% Accuracy)

🛠️ How to Run Locally
🔧 Setup
bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/heart-failure-prediction.git
cd heart-failure-prediction
pip install -r requirements.txt

🧠 Train (optional)
If you want to retrain the model:
bash
Copy
Edit
jupyter notebook heart_failure.ipynb
▶️ Run the App
bash
Copy
Edit
python app.py
Open in browser: http://127.0.0.1:5000

🌐 Deploy to Render
Steps to deploy on https://render.com:
Create a new Web Service
Connect GitHub repo

Set build command:
nginx
Copy
Edit
pip install -r requirements.txt

Set start command:
nginx
Copy
Edit
python app.py
Done! Access your live app.
