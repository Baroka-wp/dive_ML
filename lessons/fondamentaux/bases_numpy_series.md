# Domino d'exercices NumPy

_Une série de micro-défis pour apprivoiser les tableaux NumPy et leurs opérations vectorisées._

## 🎯 Objectifs
- Créer, remodeler et indexer des `ndarray` pour représenter rapidement une situation mathématique.
- Utiliser les diffusions (`broadcasting`) pour éviter les boucles lentes.
- **Prérequis bibliothèques** : NumPy.

## 🪜 Séquence d'apprentissage progressive
1. Réviser la création d'arrays (zeros, arange, reshape) avec des exemples concrets.
2. Résoudre une suite de mini-problèmes (somme cumulative, masques logiques).
3. Comparer la solution vectorisée avec une boucle Python pour voir le gain de performance.

## 🧩 Snippets à compléter
```python
import numpy as np

grains = np.zeros(100, dtype=int)
grains[0] = 1
for day in range(1, len(grains)):
    # TODO: multiplier la valeur précédente par 2
    pass

# TODO: calculer la somme totale avec grains.sum()
# TODO: afficher les 10 premiers jours pour vérifier
```

## 🔁 Variantes / exercices
- Rejouer l'exercice avec `np.power(2, np.arange(n))` pour observer l'écriture vectorisée.
- Tracer rapidement la courbe avec `matplotlib.pyplot.plot` pour visualiser la progression.
- Travailler en 2D (matrice 10×10) pour explorer `reshape` et les index multi-axes.

## 🔗 Ressources
- [Notebook local](../../NumPy_serie.ipynb) – NumPy_serie.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/NumPy_serie.ipynb)
