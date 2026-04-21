# Sprint 7 – Initialiser intelligemment k-means

_On expérimente les différentes façons de choisir les centres pour éviter des clusters bancals._

## 🎯 Objectifs
- Programmer une initialisation naïve, aléatoire puis type k-means++.
- Suivre l'évolution des centroïdes au fil des itérations.
- **Prérequis bibliothèques** : NumPy, matplotlib.

## 🪜 Séquence d'apprentissage progressive
1. Générer un nuage de points synthétique avec 3 clusters connus.
2. Implémenter `assign_points` puis `update_centroids`.
3. Comparer plusieurs seeds et mesurer l'inertie finale.

## 🧩 Snippets à compléter
```python
import numpy as np

def init_centroids(X, k, method="random"):
    # TODO: gérer les méthodes "random" et "kmeans++"
    return X[:k]

def kmeans(X, k, max_iter=10):
    centroids = init_centroids(X, k)
    for _ in range(max_iter):
        # TODO: assigner les points puis recalculer les centres
        pass
    return centroids
```

## 🔁 Variantes / exercices
- Tester k-means sur des données non sphériques et commenter les limites.
- Ajouter une visualisation animée (matplotlib FuncAnimation).
- Comparer à `sklearn.cluster.KMeans` pour vérifier les résultats.

## 🔗 Ressources
- [Notebook local](../../Sprint7.ipynb) – Sprint7.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Sprint7.ipynb)
