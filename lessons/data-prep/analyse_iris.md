# Explorer le dataset Iris

_Classique intemporel : on inspecte les longueurs de pétales pour comprendre comment séparer les fleurs._

## 🎯 Objectifs
- Charger Iris, nommer les colonnes et vérifier les unités.
- Créer des graphiques pairplot/violin pour visualiser les différences d'espèce.
- **Prérequis bibliothèques** : pandas, seaborn, scikit-learn (pour charger, si besoin).

## 🪜 Séquence d'apprentissage progressive
1. Préparer les données (features, cible) et afficher `df.describe()`.
2. Tester un classifieur simple (k-NN, LogisticRegression) et mesurer son accuracy.
3. Identifier les erreurs éventuelles et réfléchir à de nouvelles features.

## 🧩 Snippets à compléter
```python
from sklearn import datasets
import pandas as pd

iris = datasets.load_iris(as_frame=True)
df = iris.frame
# TODO: renommer les colonnes pour les rendre lisibles (petal_length, ...)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

X = df.iloc[:, :4]
y = df["target"]
# TODO: splitter, entraîner, afficher l'accuracy
```

## 🔁 Variantes / exercices
- Tester un arbre de décision et afficher la profondeur obtenue.
- Créer une feature `petal_ratio = petal_length / petal_width` et observer l'effet.
- Colorer un nuage de points selon la prédiction vs la vérité pour expliquer les erreurs.

## 🔗 Ressources
- [Notebook local](../../Data%20analysis%20of%20iris.ipynb) – Data analysis of iris.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Data%20analysis%20of%20iris.ipynb)
