# Sprint 2 – Découper les données à la main

_On réimplémente `train_test_split` pour comprendre ce qui se cache derrière les utilitaires scikit-learn._

## 🎯 Objectifs
- Coder des fonctions utilitaires (shuffle, split) sans dépendre de scikit-learn.
- Tester la robustesse via des assertions et mesurer l'aléa introduit par les seeds.
- **Prérequis bibliothèques** : Python + NumPy.

## 🪜 Séquence d'apprentissage progressive
1. Écrire `my_shuffle` puis `my_train_test_split` (indices aléatoires).
2. Vérifier la stratification manuellement en comparant les pourcentages de classes.
3. Intégrer la fonction maison dans un pipeline complet et comparer aux outils officiels.

## 🧩 Snippets à compléter
```python
import numpy as np

def my_train_test_split(X, y, test_size=0.2, seed=0):
    rng = np.random.default_rng(seed)
    indices = np.arange(len(X))
    rng.shuffle(indices)
    split = int(len(X) * (1 - test_size))
    # TODO: retourner X_train, X_test, y_train, y_test
```

## 🔁 Variantes / exercices
- Supporter des tableaux pandas (`DataFrame`) en conservant les index.
- Ajouter une option `stratify` avec des comptages numériques.
- Comparer les résultats avec scikit-learn et expliquer les éventuels écarts.

## 🔗 Ressources
- [Notebook local](../../Sprint2%20Introduction%20%C3%A0%20l%27apprentissage%20automatique%20scratch.ipynb) – Sprint2 Introduction à l'apprentissage automatique scratch.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Sprint2%20Introduction%20%C3%A0%20l%27apprentissage%20automatique%20scratch.ipynb)
