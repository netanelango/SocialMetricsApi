import pandas as pd
import mysql.connector
import pickle
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Python ne supporte pas la modification du contexte SSL (très peu de cas)
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

import nltk
nltk.download('stopwords')

nltk.download('stopwords')
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

def get_data_from_db():
    conn = mysql.connector.connect(
        host='localhost',
        user='socialmetrics_user',
        password='mon_mot_de_passe',
        database='socialmetrics'
    )
    query = "SELECT text, positive FROM tweets"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

def train():
    df = get_data_from_db()
    X = df['text']
    y = df['positive']  # On considère ici le label positif
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Récupération des stop words en français avec NLTK
    french_stop_words = stopwords.words('french')
    
    # Transformation du texte en vecteurs numériques
    vectorizer = TfidfVectorizer(stop_words=french_stop_words)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    # Entraînement du modèle de régression logistique
    model = LogisticRegression()
    model.fit(X_train_tfidf, y_train)
    
    # Affichage de la matrice de confusion et du rapport de classification
    y_pred = model.predict(X_test_tfidf)
    print("Matrice de confusion :")
    print(confusion_matrix(y_test, y_pred))
    print("\nRapport de classification :")
    print(classification_report(y_test, y_pred))
    
    # Sauvegarde du modèle et du vectorizer
    with open('sentiment_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('tfidf_vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)

if __name__ == '__main__':
    train()
