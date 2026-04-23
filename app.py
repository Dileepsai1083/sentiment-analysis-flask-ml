from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html", user_text="", prediction_text=None)

@app.route("/predict", methods=["POST"])
def predict():
    text = request.form["text"]

    cleaned = vectorizer.transform([text])
    prediction = model.predict(cleaned)[0]

    # 🔴 NEW LOGIC
    # 0 = Positive
    # 1 = Negative
    result = "Negative 😡" if prediction == 0 else "Positive 😊"

    return render_template(
        "index.html",
        prediction_text=f"Sentiment: {result}",
        user_text=text
    )

if __name__ == "__main__":
    app.run(debug=True)