# Suite géométrique – Problème de blé et d'échiquier

_Reconstitution de la légende du blé doublé sur chaque case en Python pur (listes imbriquées, aucune dépendance scientifique)._ 

## 🎯 Objectifs pédagogiques

- Programmer la progression 1, 2, 4… sur une grille en manipulant uniquement des entiers et boucles `for`.
- Calculer le total de grains et analyser la distribution sans NumPy.
- Préparer une heatmap ou un export ultérieur à partir de données natives (`list` de `list`).

## 🧱 Déroulé suggéré

1. Illustrer la règle sur un mini échiquier (2×2) pour ancrer l'intuition.
2. Étendre la logique à un échiquier n×m via deux boucles imbriquées.
3. Calculer la somme totale et explorer différentes questions (deuxième moitié, case seuil, etc.).

## 🧪 Variantes / exercices

- Modifier la règle (triple sur les colonnes impaires) et comparer les résultats.
- Ajouter une fonction qui renvoie la case où un seuil est franchi.
- Exporter la matrice dans un fichier texte/CSV pour visualisation externe.

## 🔁 Séquence d'apprentissage progressive

1. Construisez la liste de listes pour un 2×2 et affichez-la.
2. Généralisez à n×m et vérifiez la quantité sur quelques cases clés.
3. Ajoutez des fonctions utilitaires : somme totale, somme de la seconde moitié, recherche de seuil.

## 🧩 Snippets à compléter

```python
def wheat_board(rows=8, cols=8):
    board = []
    grains = 1
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(grains)
            # TODO: doubler grains pour la prochaine case
        board.append(row)
    return board

board = wheat_board()
print(sum(sum(row) for row in board))
```

## ✅ Corrigé / Notebook

- [Notebook local](../../Probl%C3%A8me%20de%20bl%C3%A9%20et%20d%27%C3%A9chiquier.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Probl%C3%A8me%20de%20bl%C3%A9%20et%20d%27%C3%A9chiquier.ipynb)
