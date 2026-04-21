# Classifier Iris en binaire

_On apprend à choisir les bonnes features pour séparer deux espèces de fleurs et mesurer l'impact de chaque choix._

## 🎯 Objectifs
- Sélectionner manuellement les colonnes les plus séparatrices (petal_length vs sepal_length).
- Comparer plusieurs classifieurs simples (LogisticRegression, SVM linéaire).
- **Prérequis bibliothèques** : pandas, NumPy, scikit-learn.

## 🪜 Séquence d'apprentissage progressive
1. Créer un sous-ensemble binaire (ex: Versicolor vs Virginica).
2. Tester 2 ou 3 modèles et tracer la frontière de décision.
3. Analyser les erreurs via une matrice de confusion commentée.

## 🧩 Snippets à compléter
```python
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

iris = datasets.load_iris()
# TODO: filtrer deux classes puis sélectionner deux features
model = LogisticRegression()
# TODO: entraîner et afficher la matrice de confusion
```

## 🔁 Variantes / exercices
- Tester un modèle non-linéaire (SVC RBF) et comparer les marges.
- Utiliser `StandardScaler` pour voir son effet sur la convergence.
- Essayer un split temporel (ordre des mesures) pour sensibiliser au surapprentissage.

## 🔗 Ressources
- [Notebook local](../../Binary%20classification%20of%20iris.ipynb) – Binary classification of iris.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Binary%20classification%20of%20iris.ipynb)
