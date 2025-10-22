<!-- <h2> 🥗 Diet Goal Predictor </h2>

<p>  smart and intuitive web application that predicts your health goal – whether it's Weight Loss, Muscle Gain, or Maintenance – based on your nutritional intake and body profile using Machine Learning. </p>

<h3> 🌟 Features </h3>

📊 Trained on real nutritional data from nutrition.csv

🤖 ML-based prediction using best of Logistic Regression or Random Forest

📈 Scaled inputs using StandardScaler for better model performance

🧠 Dynamic model loading for flexibility and performance

🧪 CLI and Web support (Flask + Tailwind CSS UI)

⚖️ Balanced dataset for fair training across all health goals

💾 All trained models and scalers are persisted with joblib

</h3>📂 Project Structure </h3>
diet-goal-predictor/ <br>
│ <br>
├── app.py                      # Flask web application <br>
├── diet_prediction.py         # Command-line prediction interface <br>
├── diet_recommendation.py     # Model training script <br>
├── nutrition.csv              # Dataset <br>
├── templates/ <br>
│   └── index.html             # Frontend HTML (Tailwind CSS) <br>
├── .gitignore <br>
└── venv/                      # Virtual environment (not included) <br>

<h3> 🚀 Getting Started </h3>
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

<h3>🧠 Model Training </h3>

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

<b> Run: </b>

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


<b>📢 Output: </b>

🥗 Recommended Health Goal: Muscle Gain

🌐 Web App (Flask + Tailwind CSS)
Run the Flask app:
python app.py


Visit: http://127.0.0.1:5000


<h4>📦 Files Saved After Training </h4>

logistic_regression_diet_model.joblib or randomforest_diet_model.joblib

scaler.joblib – for input scaling

feature_cols.joblib – list of features used

label_encoder.joblib – for decoding output

best_model_name.joblib – used by web app for dynamic loading

<h3> 🤖 Prediction Logic </h3>

The health goal is assigned using nutrient thresholds:

if calories < median and fat < median → "Weight Loss"
elif protein > median and calories > median → "Muscle Gain"
else → "Maintenance"


Made with love by ❤️ Kikani Pushkar 
Let's connect on:
    LinkedIn: https://www.linkedin.com/in/pushkar-kikani-984b0a34a/
    Instagram: https://instagram.com/itzpushkar_21 -->


  <h1>🥗 Diet Goal Predictor</h1>

  <p>
    A <strong>smart and intuitive web application</strong> that predicts your health goal – 
    whether it's <strong>Weight Loss</strong>, <strong>Muscle Gain</strong>, or 
    <strong>Maintenance</strong> – based on your nutritional intake and body profile using 
    <strong>Machine Learning</strong>.
  </p>

  <h2>🌟 Features</h2>
  <ul>
    <li>📊 Trained on real nutritional data from <code>nutrition.csv</code></li>
    <li>🤖 ML-based prediction using Logistic Regression or Random Forest</li>
    <li>📈 Input scaling via <code>StandardScaler</code> for improved performance</li>
    <li>🧠 Dynamic model loading for flexibility and performance</li>
    <li>🧪 CLI and Web (Flask + Tailwind CSS) support</li>
    <li>⚖️ Balanced dataset ensuring fair goal distribution</li>
    <li>💾 Model and scaler persistence using <code>joblib</code></li>
  </ul>

  <h2>📂 Project Structure</h2>
  <pre>
diet-goal-predictor/
│
├── app.py                  # Flask web application
├── diet_prediction.py      # Command-line prediction interface
├── diet_recommendation.py  # Model training script
├── nutrition.csv           # Dataset
├── templates/
│   └── index.html          # Frontend (Tailwind CSS)
├── .gitignore
└── venv/                   # Virtual environment (excluded)
  </pre>

  <h2>🚀 Getting Started</h2>

  <ol>
    <li><strong>Clone the repository</strong><br>
      <pre>git clone https://github.com/your-username/diet-goal-predictor.git
cd diet-goal-predictor</pre>
    </li>

    Set up virtual environment
      python -m venv venv
      source venv/bin/activate  # On Windows use venv\Scripts\activate</pre>


    Install dependencies
      pip install -r requirements.txt
      If you don’t have a requirements file:
      pip install flask scikit-learn pandas numpy joblib
    
  </ol>

  <h2>🧠 Model Training</h2>
  <p>Train the ML model using your <code>nutrition.csv</code> dataset:</p>
  <pre>python diet_recommendation.py</pre>

  <div class="highlight">
    ✔️ This will:
    <ul>
      <li>Clean and process the dataset</li>
      <li>Create synthetic <code>Age</code> and <code>BMI</code> columns</li>
      <li>Assign health goals logically</li>
      <li>Balance dataset classes</li>
      <li>Train both Logistic Regression & Random Forest models</li>
      <li>Save the best-performing model and related artifacts</li>
    </ul>
  </div>

  <h2>🔍 Predict from Command Line</h2>
  <p>Run:</p>
  <pre>python diet_prediction.py</pre>
  <p>Enter values when prompted (example):</p>
  <pre>
Age: 28
BMI: 23.5
Calories: 2200
Protein: 15
Total Fat: 3
Carbohydrate: 25
Fiber: 4
Sugar: 6
Water: 60
  </pre>

  <div class="highlight">
    📢 Output: <strong>🥗 Recommended Health Goal: Muscle Gain</strong>
  </div>

  <h2>🌐 Web App (Flask + Tailwind CSS)</h2>
  <p>Run the Flask app:</p>
  <pre>python app.py</pre>
  <p>Then visit <a href="http://127.0.0.1:5000" target="_blank">http://127.0.0.1:5000</a></p>

  <h2>📦 Files Saved After Training</h2>
  <ul>
    <li><code>logistic_regression_diet_model.joblib</code> or <code>randomforest_diet_model.joblib</code></li>
    <li><code>scaler.joblib</code> – input scaling</li>
    <li><code>feature_cols.joblib</code> – list of model features</li>
    <li><code>label_encoder.joblib</code> – label decoding</li>
    <li><code>best_model_name.joblib</code> – used for dynamic loading</li>
  </ul>

  <h2>🤖 Prediction Logic</h2>
  <pre>
if calories < median and fat < median → "Weight Loss"
elif protein > median and calories > median → "Muscle Gain"
else → "Maintenance"
  </pre>

  <h2>📌 Future Improvements</h2>
  <ul>
    <li>🧬 Integrate advanced nutrition datasets (e.g. USDA)</li>
    <li>📱 Convert to a mobile-friendly Progressive Web App (PWA)</li>
    <li>🗄️ Store user data and predictions in a database</li>
    <li>📈 Add model evaluation dashboard</li>
    <li>✅ Implement automated unit testing & CI/CD</li>
  </ul>

  <footer>
    <p>Made with ❤️ by <strong>Kikani Pushkar</strong></p>
    <p>
      <a href="https://www.linkedin.com/in/pushkar-kikani-984b0a34a/" target="_blank">LinkedIn</a> |
      <a href="https://instagram.com/itzpushkar_21" target="_blank">Instagram</a>
    </p>
  </footer>

