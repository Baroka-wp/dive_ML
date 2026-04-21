# Sprint 5 – Marges et SVM

_On découvre comment un SVM cherche la plus grande marge possible entre deux classes._

## 🎯 Objectifs
- Visualiser la géométrie des hyperplans et multiplier les exemples concrets.
- Coder (ou au moins paramétrer) un SVM linéaire et jouer avec C, kernels.
- **Prérequis bibliothèques** : NumPy, scikit-learn, matplotlib.

## 🪜 Séquence d'apprentissage progressive
1. Construire un dataset jouet (2 features) pour visualiser l'hyperplan.
2. Utiliser `sklearn.svm.SVC` et afficher les vecteurs de support.
3. Étudier les variations quand on change C ou le kernel (linéaire vs RBF).

## 🧩 Snippets à compléter
```python
from sklearn import svm
import numpy as np

X = np.random.randn(50, 2)
y = np.where(X[:, 0] + X[:, 1] > 0, 1, -1)
model = svm.SVC(kernel="linear", C=1.0)
# TODO: entraîner et récupérer model.coef_
```

## 🔁 Variantes / exercices
- Comparer SVM linéaire vs kernel RBF sur un dataset en croissant (non séparables).
- Afficher la marge avec `plt.fill_between` pour rendre la notion concrète.
- Tester un SVM multi-classes via `OneVsRestClassifier`.

## 🔗 Ressources
- [Notebook local](../../Sprint5_SVM.ipynb) – Sprint5_SVM.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Sprint5_SVM.ipynb)
