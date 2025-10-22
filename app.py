from flask import Flask, render_template, request, jsonify
import joblib
import traceback
import pandas as pd

app = Flask(__name__)

# Load Best Model and Other Files

try:
    # Load the name of the best model
    best_model_name = joblib.load("best_model_name.joblib")

    # Load the actual best model file dynamically
    model = joblib.load(f"{best_model_name.lower()}_diet_model.joblib")  
    
    # Load scaler, feature columns, and label encoder
    scaler = joblib.load("scaler.joblib")
    feature_cols = joblib.load("feature_cols.joblib")
    label_enc = joblib.load("label_encoder.joblib")

    print(f"✅ Model loaded successfully: {best_model_name}")

except Exception as e:
    print("❌ Error loading model files:", e)
    traceback.print_exc()

# Prediction Function

def predict_health_goal(user_input):
    df = pd.DataFrame([user_input])
    df = df[feature_cols]  
    df_scaled = scaler.transform(df)
    pred = model.predict(df_scaled)
    return label_enc.inverse_transform(pred)[0]

# Flask Routes

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        user_input = {k: float(v) for k, v in data.items()}
        prediction = predict_health_goal(user_input)
        return jsonify({"status": "success", "goal": prediction})
    except Exception as e:
        traceback.print_exc()
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
