# Importation des bibliothèques nécessaires
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import numpy as np

print("Étape 1: Chargement du jeu de données Iris.")
# Chargement du jeu de données Iris
iris = load_iris()
X = iris.data
y = iris.target.reshape(-1, 1) 

print("Étape 2: Encodage One-Hot des étiquettes.")
encoder = OneHotEncoder()
y_onehot = encoder.fit_transform(y).toarray()

print("Étape 3: Division du jeu de données en ensembles d'entraînement et de test.")
X_train, X_test, y_train, y_test = train_test_split(X, y_onehot, test_size=0.2, random_state=42)


print("Étape 4: Sauvegarde des ensembles d'entraînement et de test pour une utilisation ultérieure.")
np.savez('iris_data.npz', X_train=X_train, X_test=X_test, y_train=y_train, y_test=y_test)

print(f"Taille de l'ensemble d'entraînement: {X_train.shape[0]} échantillons.")
print(f"Taille de l'ensemble de test: {X_test.shape[0]} échantillons.")

print("Préparation des données terminée.")
