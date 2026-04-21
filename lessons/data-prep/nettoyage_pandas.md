# Nettoyage express avec pandas

_On s'entraîne à repérer les colonnes douteuses, imputées, et préparer un dataset prêt à modéliser._

## 🎯 Objectifs
- Diagnostiquer les variables importantes via `isna`, `value_counts`, `describe`.
- Imputer proprement (médiane, mode) et documenter les règles appliquées.
- **Prérequis bibliothèques** : pandas, NumPy, seaborn/matplotlib pour les vérifs visuelles.

## 🪜 Séquence d'apprentissage progressive
1. Lister les colonnes clés et leur rôle (identifiant, cible, feature).
2. Automatiser l'imputation + l'encodage (One-Hot, LabelEncoder).
3. Comparer la version brute vs nettoyée sur quelques graphiques simples.

## 🧩 Snippets à compléter
```python
import pandas as pd

df = pd.read_csv("housing.csv")
missing = df.isna().sum().sort_values(ascending=False)
print(missing.head())

def fill_with_median(frame, col):
    # TODO: calculer la médiane
    # TODO: remplacer les NaN par cette valeur
    return frame
```

## 🔁 Variantes / exercices
- Créer une fonction `report_duplicated_rows` qui affiche les doublons potentiels.
- Tester plusieurs stratégies d'imputation et comparer avec une métrique simple (MAE).
- Exporter un dictionnaire de données (colonne → description) en Markdown.

## 🔗 Ressources
- [Notebook local](../../Data%20cleaning%20with%20python%20pandas.ipynb) – Data cleaning with python pandas.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Data%20cleaning%20with%20python%20pandas.ipynb)
