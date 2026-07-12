import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("ml/data/synthetic_yield_dataset.csv")

# Input features
X = df[["Waste_Type", "Quantity_kg", "Location"]]

# Target values
y = df[["CBG_Yield", "Revenue", "Slurry"]]

# Categorical and numerical columns
categorical_features = ["Waste_Type", "Location"]
numerical_features = ["Quantity_kg"]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", "passthrough", numerical_features)
    ]
)

# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Pipeline
pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
pipeline.fit(X_train, y_train)

# Save model
joblib.dump(pipeline, "ml/Model/cbg_model.pkl")

print("✅ Model trained and saved successfully!")