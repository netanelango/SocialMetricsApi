import pickle

MODEL_PATH = 'sentiment_model.pkl'
VECTORIZER_PATH = 'tfidf_vectorizer.pkl'

def load_model():
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    with open(VECTORIZER_PATH, 'rb') as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

model, vectorizer = load_model()

def predict_sentiment(text):
    X = vectorizer.transform([text])
    proba = model.predict_proba(X)[0]
    # On suppose que l'indice 1 correspond à la classe positive
    # Transformation de la probabilité en score [-1, 1]
    score = 2 * (proba[1] - 0.5)
    return score
