# Sprint 3 – Régression linéaire à l'ancienne

_On part d'une fonction hypothétique et on apprend à ajuster les coefficients avec descente de gradient._

## 🎯 Objectifs
- Deriver la fonction de coût MSE et implémenter la mise à jour paramètre par paramètre.
- Tracer la droite obtenue versus les points pour visualiser l'ajustement.
- **Prérequis bibliothèques** : NumPy, matplotlib.

## 🪜 Séquence d'apprentissage progressive
1. Initialiser `theta0`, `theta1` puis définir `predict(x)`.
2. Implémenter `update_params` avec un taux d'apprentissage réglable.
3. Comparer gradient analytique vs solution fermée (`np.linalg.lstsq`).

## 🧩 Snippets à compléter
```python
import numpy as np

def gradient_step(theta, X, y, lr=0.01):
    preds = X @ theta
    errors = preds - y
    grad = (X.T @ errors) / len(X)
    # TODO: retourner theta - lr * grad
```

## 🔁 Variantes / exercices
- Ajouter la régularisation L2 et observer l'effet sur les coefficients.
- Écrire un petit tableau de bord (loss vs epoch) en texte.
- Tester l'algorithme sur un dataset bruité que tu as fabriqué.

## 🔗 Ressources
- [Notebook local](../../Sprint3_Regression_lineaire.ipynb) – Sprint3_Regression_lineaire.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Sprint3_Regression_lineaire.ipynb)
