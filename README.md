TP Final : API d'Analyse de Sentiments

Présentation

Ce projet a pour objectif de développer une API permettant d'analyser les sentiments exprimés dans des tweets. L'API reçoit une liste de tweets et renvoie pour chacun un score de sentiment allant de -1 (très négatif) à 1 (très positif). Pour ce faire, le projet intègre :

Une API Flask pour traiter les requêtes.
Un modèle de machine learning basé sur la régression logistique de scikit-learn, entraîné sur des tweets annotés.
Une base de données MySQL pour stocker les tweets annotés.
Un mécanisme de réentraînement automatique du modèle, via un script planifié (cron).
Technologies Utilisées

Python 
Flask – pour le développement de l'API.
scikit-learn – pour la régression logistique et le traitement de texte.
MySQL – pour le stockage des données annotées.
Cron – pour l'automatisation du réentraînement du modèle.
Structure du Projet

.
├── app.py                  # Code de l'API Flask
├── model.py                # Chargement du modèle et fonction de prédiction
├── train_model.py          # Script d'entraînement et de sauvegarde du modèle
├── db_setup.sql            # Script SQL pour créer la table 'tweets'
├── requirements.txt        # Liste des dépendances Python
└── README.md               # Ce fichier
Installation

Prérequis
Python 3.x installé sur votre machine.
MySQL installé et configuré.
pip pour l'installation des dépendances.
Installation des Dépendances
Installez les dépendances avec la commande suivante :

pip install -r requirements.txt
Configuration de la Base de Données MySQL
Créez une base de données (par exemple, socialmetrics).
Exécutez le script db_setup.sql pour créer la table tweets :
mysql -u <votre_username> -p <socialmetrics> < db_setup.sql
Mettez à jour les informations de connexion dans le fichier train_model.py (paramètres host, user, password, database).
Utilisation

Démarrer l'API Flask
Pour lancer l'API, exécutez :

python app.py
L'API sera disponible à l'adresse http://localhost:5000.

Endpoint de Prédiction
URL : /predict
Méthode : POST
Payload Exemple (JSON) :

{
  "tweets": [
    "Ceci est un tweet positif",
    "Ceci est un tweet négatif"
  ]
}
Réponse Exemple :

{
  "Ceci est un tweet positif": 0.8,
  "Ceci est un tweet négatif": -0.6
}
Entraînement du Modèle
Pour entraîner le modèle sur les données annotées :

python train_model.py
Ce script :

Récupère les tweets depuis la base de données MySQL.
Entraîne un modèle de régression logistique avec un TfidfVectorizer.
Affiche la matrice de confusion et le rapport de classification.
Sauvegarde le modèle et le vectorizer dans les fichiers sentiment_model.pkl et tfidf_vectorizer.pkl.
Réentraînement Automatisé
Pour automatiser le réentraînement du modèle chaque semaine, planifiez l'exécution du script train_model.py via un cron job. Par exemple, pour un réentraînement chaque dimanche à minuit, ajoutez la ligne suivante dans votre crontab :

0 0 * * 0 /usr/bin/python3 /chemin/vers/train_model.py >> /chemin/vers/train_model.log 2>&1