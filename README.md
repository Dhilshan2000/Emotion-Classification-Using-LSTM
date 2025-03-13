# Emotion Classification Using LSTM & Machine Learning

This project uses a combination of Long Short-Term Memory (LSTM) and machine learning models to classify emotions in text input. The system uses a pre-trained Logistic Regression model to classify emotions based on user input, and it presents the results through a Flask web application.

## Features
- **Emotion Prediction**: Classifies text input into various emotional categories: Anger, Fear, Joy, Love, Sadness, or Surprise.
- **Web Interface**: A simple Flask-based interface for user interaction, where users can input comments, and the model will predict the emotion based on the content.
- **Pre-trained Models**: The app uses a trained Logistic Regression model and a TF-IDF Vectorizer for text processing.

## Setup

To get started with this project, follow the instructions below:

### Prerequisites
Ensure you have the following installed:
- Python 3.6 or higher
- Flask
- NLTK
- Pickle (for model and vectorizer loading)

###How It Works
- The user enters a text comment in the provided form on the webpage.
- The text is cleaned and processed using NLTK functions (removing stopwords and stemming).
- The processed text is vectorized using the pre-trained TF-IDF vectorizer.
- The logistic regression model predicts the emotion based on the processed text.
- The predicted emotion is displayed on the webpage.
  
###Model Information

The emotion classification model is a Logistic Regression model, trained on labeled emotion data.

The categories include:

- Anger
- Fear
- Joy
- Love
- Sadness
- Surprise




