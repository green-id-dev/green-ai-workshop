# Importation des bibliothèques nécessaires
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Calcul des statistiques d'émissions pour les modèles initial et optimisé
# Supposons que les identifiants 'run_id' du modèle initial et optimisé soient connus ou déterminés d'une certaine manière
# Pour cet exemple, nous allons simplement séparer les données en deux parties égales pour représenter les modèles initial et optimisé


# Précision des modèles (exemple fictif, remplacer par les valeurs réelles obtenues)

initial_emissions = 3 # Supposons que ceci soit la précision initiale du modèle
optimized_emissions = 3.2 # Supposons une légère amélioration après optimisation

initial_accuracy = 0.90  # Supposons que ceci soit la précision initiale du modèle
optimized_accuracy = 0.92  # Supposons une légère amélioration après optimisation

# Création du DataFrame pour visualisation
data = {
    "Modèle": ["Initial", "Optimisé"],
    "Précision": [initial_accuracy, optimized_accuracy],
    "Émissions CO2 (kg)": [initial_emissions, optimized_emissions]
}

df = pd.DataFrame(data)

# Affichage du DataFrame pour vérification
print(df)

# Visualisation de la précision des modèles
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)  # Deux graphiques côte à côte, ceci est le premier
plt.bar(df["Modèle"], df["Précision"], color=['blue', 'green'])
plt.title("Précision des modèles")
plt.ylabel("Précision")
plt.ylim(0, 1)  # Limite de l'axe des y pour mieux visualiser les différences

# Visualisation des émissions de CO2
plt.subplot(1, 2, 2)  # Deux graphiques côte à côte, ceci est le second
plt.bar(df["Modèle"], df["Émissions CO2 (kg)"], color=['red', 'orange'])
plt.title("Émissions de CO2")
plt.ylabel("Émissions CO2 (kg)")
plt.ylim(0, np.nanmax(df["Émissions CO2 (kg)"]) * 1.1)  # Ajoute un peu d'espace au-dessus pour la lisibilité

plt.tight_layout()
plt.show()
