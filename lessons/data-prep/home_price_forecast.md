# Prédire les prix de l'immobilier

_On enchaîne préparation de données, modélisation et soumission Kaggle façon House Prices._

## 🎯 Objectifs
- Assembler un pipeline complet : preprocessing → modèle → export CSV.
- Comparer plusieurs algorithmes (Ridge, RandomForest, XGBoost).
- **Prérequis bibliothèques** : pandas, NumPy, scikit-learn, éventuellement XGBoost/LightGBM.

## 🪜 Séquence d'apprentissage progressive
1. Créer une classe `HousePricePipeline` (ou fonction) qui gère l'encodage + l'imputation.
2. Chercher un bon set d'hyperparamètres via GridSearchCV ou RandomizedSearchCV.
3. Exporter la prédiction finale (`submission.csv`) et noter le score public Kaggle.

## 🧩 Snippets à compléter
```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

numeric_features = ["LotArea", "GrLivArea"]  # TODO: compléter
categorical_features = ["Neighborhood", "HouseStyle"]

numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])
categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])
```

## 🔁 Variantes / exercices
- Tester `RidgeCV` ou `LGBMRegressor` et documenter l'impact sur le leaderboard.
- Créer un notebook annexe qui n'utilise que 5 features pour expliquer la différence de score.
- Comparer la performance locale (cross-val) à la note Kaggle et analyser l'écart.

## 🔗 Ressources
- [Notebook local](../../Home%20Price%20Forecast.ipynb) – Home Price Forecast.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Home%20Price%20Forecast.ipynb)
