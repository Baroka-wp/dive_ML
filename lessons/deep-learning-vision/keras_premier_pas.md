# Prendre en main Keras

_On découvre l'API Sequential/Functional et on entraîne un petit réseau dense avant de passer à plus gros._

## 🎯 Objectifs
- Configurer `model.compile` avec la bonne loss/métrique pour la tâche visée.
- Utiliser les callbacks (EarlyStopping, ModelCheckpoint).
- **Prérequis bibliothèques** : TensorFlow/Keras, NumPy.

## 🪜 Séquence d'apprentissage progressive
1. Construire un `Sequential` simple (Dense → ReLU → Dense).
2. Ajouter un callback d'arrêt anticipé et surveiller la val_loss.
3. Exporter le modèle (`model.save`) et recharger pour prédire.

## 🧩 Snippets à compléter
```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation="relu", input_shape=(20,)),
    tf.keras.layers.Dense(1, activation="sigmoid")
])
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
# TODO: appeler model.fit(X_train, y_train, validation_split=0.2, callbacks=[...])
```

## 🔁 Variantes / exercices
- Tester l'API Functional pour bâtir une architecture avec plusieurs entrées.
- Créer un modèle de régression (loss = MSE) au lieu de classification.
- Brancher TensorBoard pour visualiser l'entraînement en direct.

## 🔗 Ressources
- [Notebook local](../../keras.ipynb) – keras.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/keras.ipynb)
