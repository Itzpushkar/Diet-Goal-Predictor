import pandas as pd
import joblib

# Step 1: Load Best Model, Scaler, Feature Columns & LabelEncoder (Basically load all things from diet_recommendation
#   which are required for testing)

try:
    
    best_model_name = joblib.load("best_model_name.joblib")  # saved during training
    print(f"✅ Loading best model: {best_model_name}")

    best_model = joblib.load(f"{best_model_name.lower()}_diet_model.joblib")  
    scaler = joblib.load("scaler.joblib")
    feature_cols = joblib.load("feature_cols.joblib")
    label_enc = joblib.load("label_encoder.joblib")

except Exception as e:
    print("❌ Error loading model files:", e)
    raise

# Step 2: Prediction Function

def predict_health_goal(user_input):
    df = pd.DataFrame([user_input])
    df = df[feature_cols]
    df_scaled = scaler.transform(df)
    pred = best_model.predict(df_scaled)
    return label_enc.inverse_transform(pred)[0]

# Step 3: Dummy Example to help user to which type of data he/she should enter for prediction

example_input = {
    "Age": 25,
    "BMI": 22.5,
    "calories": 180,
    "protein": 12,
    "total_fat": 3,
    "carbohydrate": 20,
    "fiber": 4,
    "sugar": 5,
    "water": 70
}

print("🥗 Recommended Health Goal:", predict_health_goal(example_input))

# Step 4: Take input from user through cmd or terminal

print("\nEnter food/nutrition values to get recommendation (type 'exit' to quit)\n")

while True:
    age = input("Age: ")
    if age.lower() == 'exit':
        break
    bmi = input("BMI: ")
    calories = input("Calories: ")
    protein = input("Protein: ")
    total_fat = input("Total Fat: ")
    carb = input("Carbohydrate: ")
    fiber = input("Fiber: ")
    sugar = input("Sugar: ")
    water = input("Water: ")

    try:
        user_input = {
            "Age": float(age),
            "BMI": float(bmi),
            "calories": float(calories),
            "protein": float(protein),
            "total_fat": float(total_fat),
            "carbohydrate": float(carb),
            "fiber": float(fiber),
            "sugar": float(sugar),
            "water": float(water)
        }
        print("🥗 Recommended Health Goal:", predict_health_goal(user_input), "\n")
    except:
        print("❌ Invalid input. Please enter numeric values.\n")
