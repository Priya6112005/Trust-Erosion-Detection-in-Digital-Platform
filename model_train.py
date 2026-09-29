import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("processed_trust_dataset.csv")

# Convert hesitation_level to numeric
hes_map = {"Low": 0, "Medium": 1, "High": 2}
df["hesitation_level"] = df["hesitation_level"].map(hes_map)

# Select features
X = df[[
    "abandonment",
    "policy_anxiety",
    "doubt_signal",
    "hesitation_level"
]]

y = df["trust_stage"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict on test set
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# Save model
joblib.dump(model, "trust_model.pkl")
print("\nModel trained and saved successfully!")

# Feature Importance
importances = model.feature_importances_
features = X.columns

plt.figure()
plt.bar(features, importances)
plt.title("Feature Importance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("feature_importance.png")

print("Feature importance saved successfully!")
