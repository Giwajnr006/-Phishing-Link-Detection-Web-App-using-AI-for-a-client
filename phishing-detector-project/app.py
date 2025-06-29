from flask import Flask, request, render_template
import joblib
import pandas as pd
from feature_extractor import extract_features

app = Flask(__name__)
model = joblib.load('phishing_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        url = request.form['url']
        features = pd.DataFrame([extract_features(url)])
        prediction = model.predict(features)[0]
        result = "⚠️ Phishing Link Detected!" if prediction == 1 else "✅ Safe Link"
    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
