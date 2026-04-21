# Sprint 9 – Premiers réseaux neuronaux

_On assemble des couches denses, on lisse les gradients et on comprend pourquoi l'initialisation compte._

## 🎯 Objectifs
- Coder un perceptron multi-couches minimal avec NumPy.
- Tester plusieurs fonctions d'activation et schémas de lissage.
- **Prérequis bibliothèques** : NumPy, matplotlib.

## 🪜 Séquence d'apprentissage progressive
1. Initialiser les poids de manière contrôlée (Glorot, He).
2. Implémenter propagation avant puis arrière en vectorisant au maximum.
3. Tracer la loss et l'accuracy pour diagnostiquer le sur/apprentissage.

## 🧩 Snippets à compléter
```python
import numpy as np

class TinyMLP:
    def __init__(self, input_dim, hidden_dim, output_dim):
        # TODO: initialiser W1, b1, W2, b2
        pass

    def forward(self, X):
        # TODO: implémenter affine -> activation -> affine -> softmax
        return None
```

## 🔁 Variantes / exercices
- Ajouter Dropout ou BatchNorm pour stabiliser l'apprentissage.
- Comparer SGD vs Adam et noter les différences de courbe.
- Créer un dashboard minimal texte pour suivre les pertes par epoch.

## 🔗 Ressources
- [Notebook local](../../Sprint9_Neural_network.ipynb) – Sprint9_Neural_network.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Sprint9_Neural_network.ipynb)
