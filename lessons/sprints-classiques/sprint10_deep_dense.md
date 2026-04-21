# Sprint 10 – Réseaux profonds entièrement connectés

_On pousse la profondeur, on ajuste les hyperparamètres et on apprend à surveiller l'explosion des gradients._

## 🎯 Objectifs
- Empiler plusieurs couches denses et définir un schéma d'apprentissage stable.
- Mettre en place early stopping / régularisation pour éviter l'overfit.
- **Prérequis bibliothèques** : NumPy + (optionnel) frameworks comme TensorFlow/Keras.

## 🪜 Séquence d'apprentissage progressive
1. Choisir une architecture (ex: 4 couches) et initialiser proprement.
2. Suivre l'évolution des gradients pour détecter explosion/vanishing.
3. Comparer la version NumPy à une implémentation Keras pour valider.

## 🧩 Snippets à compléter
```python
import numpy as np

class DeepDenseNet:
    def __init__(self, layer_dims):
        self.params = {}
        # TODO: initialiser chaque couche avec He/Glorot

    def train(self, X, y, epochs=50, lr=1e-3):
        for epoch in range(epochs):
            # TODO: forward -> loss -> backward -> update
            pass
```

## 🔁 Variantes / exercices
- Introduire un scheduler de learning rate (cosine, step).
- Visualiser la distribution des activations pour diagnostiquer l'effet de la profondeur.
- Brancher TensorBoard (ou équivalent texte) pour compiler les métriques.

## 🔗 Ressources
- [Notebook local](../../Sprint10_Deep_neuronal_network.ipynb) – Sprint10_Deep_neuronal_network.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Sprint10_Deep_neuronal_network.ipynb)
