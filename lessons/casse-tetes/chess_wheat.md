# Suite géométrique – Problème de blé et d'échiquier

_Reconstitution de la légende du blé doublé sur chaque case : calcul pour 2×2 puis n×m, totalisation, heatmap et comparaison de méthodes (boucle, `np.append`, broadcast)._

## 🎯 Objectifs pédagogiques

- Programmer la progression 1, 2, 4… sur une grille et calculer le total de grains.
- Mettre en avant les gains de performance en vectorisant avec NumPy.
- Visualiser la distribution (heatmap log) et interpréter les régions dominantes.

## 🧱 Déroulé suggéré

1. Commencer par un échiquier 2×2 pour expliquer la règle, puis généraliser à n×m.
2. Comparer trois méthodes de génération et mesurer les temps CPU.
3. Tracer une heatmap et répondre aux questions 'combien de grains sur la seconde moitié ?'.

## 🧪 Variantes / exercices

- Introduire une règle alternative (triple sur les colonnes impaires) et comparer.
- Ajouter une fonction qui renvoie la case où un seuil de grains est franchi.
- Exporter les résultats sous forme de CSV/tableau pour insertion dans un support de cours.

## 🔁 Séquence d'apprentissage progressive

1. Illustrer la règle du doublement sur un mini échiquier pour ancrer l'intuition.
2. Porter la logique sur une matrice NumPy et calculer le total avec `np.sum`.
3. Comparer les performances des approches (boucle pure vs. vectorisation) et tracer une heatmap log.
## 🧩 Snippets à compléter

```python
import numpy as np

def wheat_board(rows=8, cols=8):
    board = np.zeros((rows, cols), dtype=np.uint64)
    grains = 1
    for i in range(rows):
        for j in range(cols):
            board[i, j] = grains
            # TODO: doubler la quantité pour la case suivante
    return board

board = wheat_board()
print(board.sum())
```
## ✅ Corrigé / Notebook

- [Notebook local](../../Probl%C3%A8me%20de%20bl%C3%A9%20et%20d%27%C3%A9chiquier.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Probl%C3%A8me%20de%20bl%C3%A9%20et%20d%27%C3%A9chiquier.ipynb)
