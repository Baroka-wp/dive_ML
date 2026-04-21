# Cartes 2D et gradients

_On construit une grille numérique puis on mesure comment une valeur varie d'une case à l'autre, comme une carte météo discrète._

## 🎯 Objectifs
- Créer un maillage 2D et y stocker une fonction (plan, relief, température).
- Approcher le gradient en calculant les différences entre cases voisines.
- **Prérequis bibliothèques** : Python + NumPy.

## 🪜 Séquence d'apprentissage progressive
1. Initialiser un tableau 2D `np.zeros` et remplir chaque case avec f(x, y).
2. Programmer une fonction `finite_diff` qui retourne les variations selon x puis y.
3. Visualiser ou interpréter les zones de pente forte / faible.

## 🧩 Snippets à compléter
```python
import numpy as np

def build_landscape(size=50):
    grid = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            # TODO: définir une fonction de hauteur, ex : 0.1*i + 0.05*j
            grid[i, j] = 0
    return grid

def finite_diff(grid):
    # TODO: utiliser np.diff pour approximer le gradient
    grad_x = None
    grad_y = None
    return grad_x, grad_y
```

## 🔁 Variantes / exercices
- Tester plusieurs fonctions (plan incliné, bosse gaussienne) et comparer les gradients.
- Colorer les zones de pente forte avec `matplotlib.pyplot.imshow`.
- Introduire des conditions aux bords (wrap, padding) pour modéliser un tore.

## 🔗 Ressources
- [Notebook local](../../Two-dimensional%20array%20and%20gradient%20problem.ipynb) – Two-dimensional array and gradient problem.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Two-dimensional%20array%20and%20gradient%20problem.ipynb)
