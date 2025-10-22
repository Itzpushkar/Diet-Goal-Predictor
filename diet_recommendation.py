import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.utils import resample
import joblib

# Step 1: Load Dataset (nutrition.csv)

data = pd.read_csv("nutrition.csv")

# Step 2: Extracting or collecting required nutrients from the dataset

useful_cols = ['calories', 'protein', 'total_fat', 'carbohydrate', 'fiber', 'sugar', 'water']
useful_cols = [c for c in useful_cols if c in data.columns]
df = data[useful_cols].copy()

# Step 2.1: Clean and convert nutrients units into numeric values

for col in useful_cols:
    df[col] = (
        df[col].astype(str)
        .str.replace('g', '', regex=False)
        .str.replace('mg', '', regex=False)
        .str.replace('kcal', '', regex=False)
    )
    df[col] = pd.to_numeric(df[col], errors='coerce')

df.fillna(df.mean(numeric_only=True), inplace=True)

# Step 3: Generating synthetic or the information which is required for training but not is in dataset

np.random.seed(42)
df['Age'] = np.random.randint(18, 60, size=len(df))
df['BMI'] = np.random.uniform(18.5, 30.0, size=len(df))

# Step 4: Predicting the goal or output with some basic checks

c_median = df['calories'].median()
p_median = df['protein'].median()
f_median = df['total_fat'].median()

def assign_goal(row):
    if row['calories'] < c_median and row['total_fat'] < f_median:
        return 'Weight Loss'
    elif row['protein'] > p_median and row['calories'] > c_median:
        return 'Muscle Gain'
    else:
        return 'Maintenance'

df['HealthGoal'] = df.apply(assign_goal, axis=1)

print("\n🏷️ Health Goal Distribution before balancing:")
print(df['HealthGoal'].value_counts(), "\n")

# Step 5: Converting or Encoding the target

label_enc = LabelEncoder()
df['HealthGoalEncoded'] = label_enc.fit_transform(df['HealthGoal'])

# Step 6: Balance the Dataset

df_balanced = pd.concat([
    resample(df[df['HealthGoal'] == label],
             replace=True,
             n_samples=df['HealthGoal'].value_counts().max(),
             random_state=42)
    for label in df['HealthGoal'].unique()
])

print("🏷️ Health Goal Distribution after balancing:")
print(df_balanced['HealthGoal'].value_counts(), "\n")

# Step 7: Prepare Features and Target

feature_cols = ['Age', 'BMI'] + useful_cols
X = df_balanced[feature_cols]
y = label_enc.transform(df_balanced['HealthGoal'])

# Step 8: Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 9: Scale Features

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 10: Train Models

models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42)
}

results = {}
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    results[name] = acc
    print(f"📊 {name} Accuracy: {acc:.4f}")
    print(classification_report(y_test, y_pred, target_names=label_enc.classes_))
    print("-" * 60)

# Step 11: Save Best Model and Supporting Files

best_model_name = max(results, key=results.get)
best_model = models[best_model_name]

# Save the model and other objects
joblib.dump(best_model, f"{best_model_name.lower()}_diet_model.joblib")
joblib.dump(scaler, "scaler.joblib")
joblib.dump(feature_cols, "feature_cols.joblib")
joblib.dump(label_enc, "label_encoder.joblib")

# Save best model name for dynamic loading in Flask
joblib.dump(best_model_name, "best_model_name.joblib")

print(f"\n✅ Training completed. Best model: {best_model_name} ({results[best_model_name]:.4f})")
print("💾 Model, scaler, feature columns, LabelEncoder, and best model name saved successfully.")
