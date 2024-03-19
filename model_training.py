# Importation des bibliothèques nécessaires
import tensorflow as tf
import numpy as np
from codecarbon import EmissionsTracker

# Chargement des données préparées
data = np.load('iris_data.npz')
X_train, X_test, y_train, y_test = data['X_train'], data['X_test'], data['y_train'], data['y_test']

# Définition du modèle plus complexe
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Démarrage du tracker d'émissions de CodeCarbon
tracker = EmissionsTracker()
tracker.start()

print("Début de l'entraînement du modèle.")
# Entraînement du modèle
history = model.fit(X_train, y_train, epochs=100, batch_size=16, validation_split=0.2, verbose=2)

# Arrêt du tracker et affichage des émissions
emissions = tracker.stop()
print(f"Émissions de CO2 estimées pour l'entraînement du modèle : {emissions} kg")

# Évaluation du modèle sur l'ensemble de test
print("Évaluation du modèle sur l'ensemble de test.")
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=2)
print(f"Test accuracy: {test_accuracy}")

# Optionnellement, sauvegardez le modèle pour une utilisation dans l'optimisation
model.save('my_initial_model.keras')
