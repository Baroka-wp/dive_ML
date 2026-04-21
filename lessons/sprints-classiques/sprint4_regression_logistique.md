# Sprint 4 – Logistique et probabilités

_On transforme des prédictions en probabilités et on apprend à interpréter la courbe sigmoïde._

## 🎯 Objectifs
- Définir la fonction logistique et calculer la log-loss.
- Implémenter une descente de gradient adaptée à cette nouvelle loss.
- **Prérequis bibliothèques** : NumPy, matplotlib, scikit-learn pour la validation.

## 🪜 Séquence d'apprentissage progressive
1. Coder `sigmoid(z)` puis `predict_proba`.
2. Boucler sur les epochs pour ajuster les poids et suivre la log-loss.
3. Comparer les performances à `sklearn.linear_model.LogisticRegression`.

## 🧩 Snippets à compléter
```python
import numpy as np

def sigmoid(z):
    # TODO: renvoyer 1 / (1 + exp(-z))
    return z

def log_loss(y_true, y_pred):
    # TODO: implémenter la negative log-likelihood
    pass
```

## 🔁 Variantes / exercices
- Ajouter une régularisation L1 (lasso) et comparer sparsité des poids.
- Visualiser la frontière de décision en 2D pour comprendre la marge.
- Tester l'impact d'un apprentissage avec bruit sur la cible.

## 🔗 Ressources
- [Notebook local](../../Sprint4_Regression_Logistique.ipynb) – Sprint4_Regression_Logistique.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Sprint4_Regression_Logistique.ipynb)
