🥗 Diet Goal Predictor

A smart and intuitive web application that predicts your health goal – whether it's Weight Loss, Muscle Gain, or Maintenance – based on your nutritional intake and body profile using Machine Learning.

🌟 Features

📊 Trained on real nutritional data from nutrition.csv

🤖 ML-based prediction using best of Logistic Regression or Random Forest

📈 Scaled inputs using StandardScaler for better model performance

🧠 Dynamic model loading for flexibility and performance

🧪 CLI and Web support (Flask + Tailwind CSS UI)

⚖️ Balanced dataset for fair training across all health goals

💾 All trained models and scalers are persisted with joblib

📂 Project Structure
diet-goal-predictor/
│
├── app.py                      # Flask web application
├── diet_prediction.py         # Command-line prediction interface
├── diet_recommendation.py     # Model training script
├── nutrition.csv              # Dataset
├── templates/
│   └── index.html             # Frontend HTML (Tailwind CSS)
├── .gitignore
└── venv/                      # Virtual environment (not included)

🚀 Getting Started
1. Clone the repository
git clone https://github.com/your-username/diet-goal-predictor.git
cd diet-goal-predictor

2. Set up the virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies
pip install -r requirements.txt


If you don’t have requirements.txt, create it with:

flask
scikit-learn
pandas
numpy
joblib

🧠 Model Training

To train the ML model using the nutrition.csv dataset:

python diet_recommendation.py


✔️ This will:

Clean and process the data

Create synthetic Age and BMI columns

Assign goals based on nutrient logic

Balance dataset

Train two models (LogisticRegression, RandomForest)

Save the best performing model + scaler, encoder, and feature columns

🔍 Predict from Command Line

Run:

python diet_prediction.py


Enter the values when prompted:

Age: 28
BMI: 23.5
Calories: 220
Protein: 15
Total Fat: 3
Carbohydrate: 25
Fiber: 4
Sugar: 6
Water: 60


📢 Output:

🥗 Recommended Health Goal: Muscle Gain

🌐 Web App (Flask + Tailwind CSS)
Run the Flask app:
python app.py


Visit: http://127.0.0.1:5000

UI Snapshot:

📦 Files Saved After Training

logistic_regression_diet_model.joblib or randomforest_diet_model.joblib

scaler.joblib – for input scaling

feature_cols.joblib – list of features used

label_encoder.joblib – for decoding output

best_model_name.joblib – used by web app for dynamic loading

🤖 Prediction Logic

The health goal is assigned using nutrient thresholds:

if calories < median and fat < median → "Weight Loss"
elif protein > median and calories > median → "Muscle Gain"
else → "Maintenance"

📌 Future Improvements

🧬 Use advanced nutrition datasets (e.g. USDA)

📱 Make the app mobile-friendly (PWA)

🗄️ Store user data and predictions in a DB

📈 Model evaluation dashboard

✅ Add unit testing and CI/CD

Made with love by ❤️ Kikani Pushkar 
Let's connect on:
    LinkedIn: https://www.linkedin.com/in/pushkar-kikani-984b0a34a/
    Instagram: https://instagram.com/itzpushkar_21