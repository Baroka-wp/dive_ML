# Analyser un marché immobilier

_À partir de données de logements, on apprend à sélectionner les variables pertinentes pour expliquer les prix._

## 🎯 Objectifs
- Repérer les colonnes utiles (surface, quartier, année) et les trier par importance perçue.
- Mettre en place des visualisations rapides (scatter plots, boxplots).
- **Prérequis bibliothèques** : pandas, NumPy, Matplotlib/Seaborn.

## 🪜 Séquence d'apprentissage progressive
1. Charger le dataset et filtrer les colonnes brutes (type numérique/catégoriel).
2. Créer 2 à 3 graphes clés montrant corrélations ou distributions.
3. Rédiger une mini-conclusion : quelles variables semblent conduire le prix ?

## 🧩 Snippets à compléter
```python
import pandas as pd
import seaborn as sns

df = pd.read_csv("analysis_housing.csv")
important_cols = ["surface", "prix", "quartier"]
# TODO: vérifier que toutes les colonnes existent

sns.scatterplot(data=df, x="surface", y="prix", hue="quartier")
# TODO: afficher la figure et interpréter
```

## 🔁 Variantes / exercices
- Créer un score composite (prix / surface) pour comparer les quartiers.
- Tester une régression simple `np.polyfit` pour estimer le prix selon la surface.
- Traduire l'analyse en infographie ou poster pour la classe.

## 🔗 Ressources
- [Notebook local](../../Analysis%20of%20housing%20information.ipynb) – Analysis of housing information.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Analysis%20of%20housing%20information.ipynb)
