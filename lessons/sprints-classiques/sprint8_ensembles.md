# Sprint 8 – Ensembles et votes

_Bagging, boosting : on combine plusieurs modèles pour obtenir une prédiction plus robuste._

## 🎯 Objectifs
- Assembler plusieurs estimateurs faibles et suivre l'effet sur la variance/biais.
- Coder un vote majoritaire simple avant d'utiliser les classes scikit-learn.
- **Prérequis bibliothèques** : pandas, scikit-learn (RandomForest, GradientBoosting).

## 🪜 Séquence d'apprentissage progressive
1. Créer un dataset bruité qui justifie l'utilisation d'un ensemble.
2. Implémenter un bagging artisanal (bootstrap + moyenne des prédictions).
3. Comparer RandomForestClassifier, GradientBoostingClassifier et XGBoost.

## 🧩 Snippets à compléter
```python
from sklearn.tree import DecisionTreeClassifier
import numpy as np

def bagging_predict(base_model, X, y, n_estimators=5):
    preds = []
    for _ in range(n_estimators):
        # TODO: tirer un bootstrap sample
        # TODO: entraîner un clone du modèle
        # TODO: stocker les prédictions
        pass
    # TODO: retourner la prédiction majoritaire
```

## 🔁 Variantes / exercices
- Ajouter un poids aux modèles qui performent mieux sur une validation interne.
- Comparer bagging vs boosting sur un dataset irrégulier.
- Créer un schéma qui illustre le vote majoritaire pour ta classe.

## 🔗 Ressources
- [Notebook local](../../Sprint8_apprentissage_d%27ensemble.ipynb) – Sprint8_apprentissage_d'ensemble.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Sprint8_apprentissage_d%27ensemble.ipynb)
