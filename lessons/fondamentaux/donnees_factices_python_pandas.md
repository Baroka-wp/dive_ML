# Fabriquer ses propres jeux de données

_On joue à l'apprenti statisticien : on invente un tableau réaliste pour tester ses algos sans attendre un vrai dataset._

## 🎯 Objectifs
- Construire une table synthétique (listes Python ou DataFrame pandas) avec des colonnes cohérentes.
- Introduire un peu d'aléatoire contrôlé pour simuler plusieurs scénarios.
- **Prérequis bibliothèques** : Python, `random`, `pandas` et éventuellement `numpy`.

## 🪜 Séquence d'apprentissage progressive
1. Lister les variables que l'on veut suivre (âge, score, niveau, etc.).
2. Coder une fonction qui génère N lignes en respectant des bornes ou distributions.
3. Visualiser quelques stats descriptives (moyenne, histogramme) pour vérifier la crédibilité du jeu.

## 🧩 Snippets à compléter
```python
import random
import pandas as pd

def build_synthetic_students(n_rows=20):
    records = []
    for student_id in range(n_rows):
        # TODO: tirer un âge entre 11 et 17 ans
        # TODO: attribuer un niveau ("6e", "5e", ...) selon l'âge
        # TODO: générer un score avec random.gauss(mean, std)
        records.append({
            "id": student_id,
            "age": None,
            "niveau": None,
            "score": None
        })
    return pd.DataFrame(records)

df = build_synthetic_students()
print(df.head())
```

## 🔁 Variantes / exercices
- Ajouter une date (`pd.date_range`) pour simuler un suivi hebdomadaire.
- Introduire une colonne cible (succès/échec) afin d'entraîner plus tard un classifieur.
- Écrire un export `df.to_csv('jeu_synthetique.csv', index=False)` pour partager la création.

## 🔗 Ressources
- [Notebook local](../../Creating%20dummy%20data.ipynb) – Creating dummy data.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Creating%20dummy%20data.ipynb)
- [Notebook local](../../creation_de_donnees.ipynb) – creation_de_donnees.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/creation_de_donnees.ipynb)
