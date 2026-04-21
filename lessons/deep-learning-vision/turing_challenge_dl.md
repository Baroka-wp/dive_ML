# Turing Challenge – consolider ses réflexes

_Une série de mini-exercices pour combiner POO, manipulation de données et premiers blocs de deep learning._

## 🎯 Objectifs
- Structurer le code en classes (datasets, modèles) pour gagner en clarté.
- Implémenter rapidement un perceptron ou un réseau dense pour tester les idées.
- **Prérequis bibliothèques** : Python, NumPy, (optionnel) PyTorch/TensorFlow selon les cellules.

## 🪜 Séquence d'apprentissage progressive
1. Résoudre les défis Python (fonctions, classes) pour préparer la suite.
2. Convertir ces briques en modules réutilisables (dataset loader, trainer).
3. Brancher un mini-réseau puis documenter les tests réalisés.

## 🧩 Snippets à compléter
```python
class ChallengeDataset:
    def __init__(self, csv_path):
        # TODO: charger le CSV, stocker X et y
        pass

    def batch(self, size=32):
        # TODO: générer des mini-lots aléatoires
        pass

class TinyPerceptron:
    def __init__(self, input_dim):
        # TODO: initialiser les poids
        pass

    def train(self, X, y, epochs=100):
        # TODO: boucle d'entraînement avec mise à jour des poids
        pass
```

## 🔁 Variantes / exercices
- Ajouter un logger qui trace la perte à chaque round de challenge.
- Construire une interface CLI pour lancer différents sous-défis.
- Documenter dans un carnet de bord ce que chaque mini-exercice t'a appris.

## 🔗 Ressources
- [Notebook local](../../TURING%20CHALLENG.ipynb) – TURING CHALLENG.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/TURING%20CHALLENG.ipynb)
