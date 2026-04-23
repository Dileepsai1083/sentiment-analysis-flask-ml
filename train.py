import pandas as pd
import re
import pickle
import nltk

nltk.download('stopwords')

from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("twitter.csv")

# Clean column names
data.columns = data.columns.str.strip()

print("Columns:", data.columns)

TEXT_COLUMN = "tweet"
LABEL_COLUMN = "label"

# 🔥 IMPORTANT: REVERSE LABELS
# original: 0=negative, 1=positive
# new: 0=positive, 1=negative
data[LABEL_COLUMN] = data[LABEL_COLUMN].apply(lambda x: 0 if x == 1 else 1)

# Clean text
stop_words = set(stopwords.words('english'))

def clean_text(text):
    text = str(text)
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text)
    text = text.lower()
    text = " ".join([word for word in text.split() if word not in stop_words])
    return text

data['clean_text'] = data[TEXT_COLUMN].apply(clean_text)

# Features & labels
X = data['clean_text']
y = data[LABEL_COLUMN]

# Vectorize
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Model trained successfully with NEW label mapping!")