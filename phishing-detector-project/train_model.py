import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
from feature_extractor import extract_features

# Load and process dataset
df = pd.read_csv('dataset.csv')
df_features = pd.DataFrame([extract_features(url) for url in df['url']])
df_features['label'] = df['label']

X = df_features.drop('label', axis=1)
y = df_features['label']

# Train and save model
model = RandomForestClassifier()
model.fit(X, y)
joblib.dump(model, 'phishing_model.pkl')
print("Model saved as phishing_model.pkl")
