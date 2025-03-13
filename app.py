from flask import Flask, render_template, request
import pickle
import re
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import numpy as np
# Download NLTK stopwords
nltk.download('stopwords')
stopwords = set(nltk.corpus.stopwords.words('english'))

app = Flask(__name__)

#========================loading the save files==================================================
lg = pickle.load(open('logistic_regression.pkl','rb'))
tfidf_vectorizer = pickle.load(open('tfidfvectorizer.pkl','rb'))
lb = pickle.load(open('label_encoder.pkl','rb'))

# =========================repeating the same functions==========================================
def clean_text(text):
    stemmer = PorterStemmer()
    text = re.sub("[^a-zA-Z]", " ", text)
    text = text.lower()
    text = text.split()
    text = [stemmer.stem(word) for word in text if word not in stopwords]
    return " ".join(text)
def predict_emotion(input_text):
    print(input_text)
    cleaned_text = clean_text(input_text)
    input_vectorized = tfidf_vectorizer.transform([cleaned_text])
    # Predict emotion
    predicted_label = lg.predict(input_vectorized)[0]
    predicted_emotion = lb.inverse_transform([predicted_label])[0]
    label =  np.max(lg.predict(input_vectorized))

    return predicted_emotion,label


@app.route('/', methods=['GET', 'POST'])
def analyze_emotion():
    if request.method == 'POST':
        comment = request.form.get('comment')
        predicted_emotion, label = predict_emotion(input_text=comment)
        print(label)
        return render_template('index.html', sentiment=label)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)