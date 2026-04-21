# Premiers pas avec Jupyter & Colab

_Découvre comment exécuter tes toutes premières cellules de code et structurer un carnet lisible, comme un vrai labo numérique._

## 🎯 Objectifs
- Ouvrir un notebook local ou Colab et comprendre la différence entre cellules Markdown et Python.
- Manipuler des variables, listes et boucles pour raconter une mini-histoire de données.
- **Prérequis bibliothèques** : Python standard uniquement.

## 🪜 Séquence d'apprentissage progressive
1. Prendre en main l'interface (raccourcis de base, exécution cellule par cellule).
2. Créer un mini-journal d'observations avec du texte formaté + des impressions Python.
3. Organiser le carnet avec des sections, puis sauvegarder / partager le notebook.

## 🧩 Snippets à compléter
```python
# Cellule 1 : variables et impression
secret_number = 12
guess = 0
# TODO: demander une valeur à l'utilisateur ou définir un essai
# TODO: comparer guess et secret_number puis afficher un message personnalisé

# Cellule 2 : mini-tableau
experiments = []
for minute in range(0, 11, 5):
    # TODO: ajouter un tuple (minute, valeur_mesuree)
    pass
print(experiments)
```

## 🔁 Variantes / exercices
- Ajouter un graphique rapide avec `matplotlib` si disponible pour montrer l'évolution d'une mesure.
- Insérer une image ou un lien externe dans la cellule Markdown pour raconter un contexte scientifique.
- Créer une fonction `def` qui formate automatiquement un rapport d'expérience.

## 🔗 Ressources
- [Notebook local](../../first_notebook.ipynb) – first_notebook.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/first_notebook.ipynb)
- [Notebook local](../../first_colab.ipynb) – first_colab.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/first_colab.ipynb)
