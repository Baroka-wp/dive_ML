# Construire son premier ConvNet 2D

_On prépare un dataset image simple et on implémente une architecture convolution → pooling → dense._

## 🎯 Objectifs
- Normaliser les pixels et créer des batchs prêts à l'entraînement.
- Empiler conv + relu + pooling avant d'aplatir dans une couche dense.
- **Prérequis bibliothèques** : TensorFlow/Keras ou PyTorch.

## 🪜 Séquence d'apprentissage progressive
1. Charger les images (MNIST, fruits, dessins) et créer un `DataLoader` ou `ImageDataGenerator`.
2. Définir l'architecture (conv 3×3, maxpool, dropout).
3. Suivre accuracy/val_accuracy et ajuster les hyperparamètres.

## 🧩 Snippets à compléter
```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, 3, activation="relu", input_shape=(28, 28, 1)),
    # TODO: ajouter MaxPool2D
    # TODO: empiler une seconde couche conv
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(10, activation="softmax")
])
```

## 🔁 Variantes / exercices
- Ajouter des couches de régularisation (Dropout, BatchNorm).
- Comparer optimizers (Adam, RMSprop) sur la même architecture.
- Tester des augmentations simples (flip, rotation) et noter l'effet.

## 🔗 Ressources
- [Notebook local](../../SimpleConv2d.ipynb) – SimpleConv2d.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/SimpleConv2d.ipynb)
