# Manipuler un jeu d'entraînement étape par étape

_On ouvre un DataFrame, on explore ses colonnes puis on fabrique des features propres à alimenter nos modèles._

## 🎯 Objectifs
- Charger un CSV, vérifier les types et comprendre la structure individus/variables.
- Écrire des fonctions utilitaires pour normaliser, regrouper ou concaténer des colonnes.
- **Prérequis bibliothèques** : pandas, NumPy, éventuellement Matplotlib.

## 🪜 Séquence d'apprentissage progressive
1. Importer les données (`pd.read_csv`) et afficher un résumé (head, info, describe).
2. Nettoyer/transformer : valeurs manquantes, colonnes dérivées, encodage catégoriel.
3. Exporter le jeu préparé vers un nouveau CSV ou l'envoyer à un modèle simple.

## 🧩 Snippets à compléter
```python
import pandas as pd

df = pd.read_csv("./data.csv")
# TODO: afficher les 3 premières lignes
# TODO: identifier les colonnes avec df.dtypes

def normalize_column(frame, col):
    series = frame[col]
    # TODO: retourner (series - mean) / std
    return series
```

## 🔁 Variantes / exercices
- Ajouter une vérification automatique qui alerte si une colonne possède >30% de valeurs manquantes.
- Écrire un mini-reporting texte qui résume les stats principales par colonne.
- Comparer deux sources (train/test) pour détecter un décalage de distribution.

## 🔗 Ressources
- [Notebook local](../../Training_data_manipulation.ipynb) – Training_data_manipulation.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Training_data_manipulation.ipynb)
