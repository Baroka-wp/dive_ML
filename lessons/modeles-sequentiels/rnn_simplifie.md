# RNN simple et propagation

_On implémente un SimpleRNN à la main pour comprendre comment l'information circule d'un pas de temps à l'autre._

## 🎯 Objectifs
- Programmer la propagation avant d'un RNN et visualiser les états cachés.
- Observer comment la longueur de séquence influence la mémoire du modèle.
- **Prérequis bibliothèques** : NumPy, (optionnel) TensorFlow/PyTorch pour comparer.

## 🪜 Séquence d'apprentissage progressive
1. Créer une séquence jouet (caractères, pas de temps) et définir l'encodage one-hot.
2. Coder `step(h_prev, x_t)` puis boucler sur toute la séquence.
3. Ajouter la rétropropagation temporelle simplifiée ou comparer à `tf.keras.layers.SimpleRNN`.

## 🧩 Snippets à compléter
```python
import numpy as np

class SimpleRNNLayer:
    def __init__(self, input_dim, hidden_dim):
        # TODO: initialiser Wx, Wh, b
        pass

    def step(self, x_t, h_prev):
        # TODO: calculer h_t = tanh(Wx @ x_t + Wh @ h_prev + b)
        return h_prev
```

## 🔁 Variantes / exercices
- Essayer différentes fonctions d'activation (tanh vs ReLU).
- Ajouter une couche Dense de sortie pour faire de la prédiction de symboles.
- Comparer manuellement les états à ceux renvoyés par Keras pour la même séquence.

## 🔗 Ressources
- [Notebook local](../../R%C3%A9seau_de_neurones_r%C3%A9current_%28RNN%29_.ipynb) – Réseau_de_neurones_récurrent_(RNN)_.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/R%C3%A9seau_de_neurones_r%C3%A9current_%28RNN%29_.ipynb)
