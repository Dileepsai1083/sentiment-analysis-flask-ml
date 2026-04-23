💬 Sentiment Analysis Web App (ML + Flask)
This project is a Machine Learning-based web application that predicts the sentiment of tweets (Positive 😊 or Negative 😡) using Natural Language Processing (NLP).

---

🚀 Features

🔮 Real-time sentiment prediction
🧠 Machine Learning model using Naive Bayes
🧹 Text preprocessing (cleaning, stopwords removal)
🌐 Flask-based web application
🎨 Responsive UI with Bootstrap
✨ Animated result display
🔄 Clear button to reset input and result

---

🛠 Tech Stack
Python
Pandas, NumPy
Scikit-learn
NLTK
Flask
HTML, CSS, Bootstrap

---
📊 How It Works
1. Load Twitter dataset
2. Clean text (remove URLs, special characters, stopwords)
3. Convert text into numerical features using CountVectorizer
4. Train Naive Bayes classifier
5. Save model using pickle
6. Build Flask app for user input
7. Predict sentiment and display result
---
📁 Project Structure
sentiment-analysis-flask-ml/
│── app.py
│── train.py
│── twitter.csv
│── model.pkl
│── vectorizer.pkl
│── requirements.txt
│── README.md

└── templates/
└── index.html
---
⚙️ Installation & Setup
1. Clone Repository
```bash
git clone https://github.com/your-username/sentiment-analysis-flask-ml.git
cd sentiment-analysis-flask-ml
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```
3. Train Model
```bash
python train.py
```
4. Run App
```bash
python app.py
```
5. Open Browser
http://127.0.0.1:5000/
---
🧪 Sample Inputs

| Input Text               | Output      |
| ------------------------ | ----------- |
| I love this product      | Positive 😊 |
| This is terrible service | Negative 😡 |
---
SCREENSHOTS

positive
<img width="2050" height="910" alt="positive" src="https://github.com/user-attachments/assets/10795371-362f-440c-93fd-b37bb7f0650b" />

negative
<img width="2111" height="1182" alt="Negative" src="https://github.com/user-attachments/assets/19bea843-90f1-4860-9a28-2155b2a48558" />

---

🎯 Key Learnings

Importance of text preprocessing in NLP
Feature extraction using CountVectorizer
Model training using Naive Bayes
Integrating ML model with Flask
Building interactive web applications

---

🚀 Future Improvements
📊 Add accuracy display
🌳 Use advanced models (Random Forest, LSTM, BERT)
📍 Improve handling of sarcasm
🌐 Deploy online

---
⭐ If you like this project, give it a star!
