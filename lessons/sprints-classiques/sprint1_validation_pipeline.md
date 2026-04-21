# Sprint 1 – Construire un pipeline fiable

_On découvre la validation croisée et on apprend à découper un problème en étapes reproductibles._

## 🎯 Objectifs
- Programmer une fonction de validation simple (train/test split) et interpréter ses limites.
- Documenter un pipeline de bout en bout : préparation → modèle → évaluation.
- **Prérequis bibliothèques** : Python, NumPy, scikit-learn (optionnel).

## 🪜 Séquence d'apprentissage progressive
1. Définir les objectifs (prédire ? classer ?), puis choisir les métriques.
2. Implémenter puis tester plusieurs stratégies de validation (k-fold, hold-out).
3. Remplir un log d'expériences pour suivre les scores par itération.

## 🧩 Snippets à compléter
```python
import numpy as np

def kfold_validate(model_cls, X, y, n_splits=5):
    scores = []
    # TODO: découper X, y en k sous-ensembles
    # TODO: entraîner et stocker la métrique à chaque fois
    return scores
```

## 🔁 Variantes / exercices
- Comparer validation simple vs shuffle split sur un dataset déséquilibré.
- Ajouter une contrainte temps maximal par expérimentation.
- Écrire une carte mentale du pipeline pour en faire un poster pédagogique.

## 🔗 Ressources
- [Notebook local](../../Sprint1-Flux%20d%27apprentissage%20automatique.ipynb) – Sprint1-Flux d'apprentissage automatique.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Sprint1-Flux%20d%27apprentissage%20automatique.ipynb)
