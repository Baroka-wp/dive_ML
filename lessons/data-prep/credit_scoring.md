# Comprendre et scorer les dossiers de crédit

_On décortique un concours Kaggle Home Credit : exploration, features financières et essais de modèles._

## 🎯 Objectifs
- Lire la documentation et traduire les règles métier (délai, défaut, catégories).
- Préparer des indicateurs clients (revenu, ratio dettes, stabilité d'emploi).
- **Prérequis bibliothèques** : pandas, NumPy, scikit-learn / LightGBM.

## 🪜 Séquence d'apprentissage progressive
1. Construire un data dictionary simple à partir des colonnes brutes.
2. Coder des features agrégées (moyenne par client, totaux cumulés).
3. Tester plusieurs modèles (LogisticRegression, GradientBoosting) et comparer ROC AUC.

## 🧩 Snippets à compléter
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.ensemble import GradientBoostingClassifier

df = pd.read_csv("credit_train.csv")
target = df["TARGET"]
features = df.drop(columns=["TARGET"])
# TODO: sélectionner 5 colonnes pertinentes

X_train, X_valid, y_train, y_valid = train_test_split(features, target, stratify=target)
model = GradientBoostingClassifier()
# TODO: entraîner puis calculer roc_auc_score
```

## 🔁 Variantes / exercices
- Comparer `GradientBoostingClassifier` avec `LGBMClassifier` ou `XGBClassifier`.
- Écrire une fonction `plot_feature_importance` et commenter le top 10.
- Proposer une charte éthique : comment éviter les discriminations ?

## 🔗 Ressources
- [Notebook local](../../Credit%20information%20analysis.ipynb) – Credit information analysis.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Credit%20information%20analysis.ipynb)
- [Notebook local](../../Credit%20information%20learning.ipynb) – Credit information learning.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Credit%20information%20learning.ipynb)
