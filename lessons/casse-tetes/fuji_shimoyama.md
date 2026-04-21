# Descente de montagne – Fuji Shimoyama

_reproduction d'une descente gloutonne en Python pur : matrices représentées par des listes imbriquées, aucun NumPy requis._

## 🎯 Objectifs pédagogiques

- Charger une grille d'altitudes via le module `csv` et la représenter comme liste de listes.
- Programmer des fonctions `local_slope` et `next_step` avec uniquement des boucles/conditions Python.
- Comparer les trajectoires obtenues en modifiant point de départ et règles d'arrêt.

## 🧱 Déroulé suggéré

1. Charger `mtfuji_data.csv` avec `csv.reader` et afficher quelques lignes pour vérifier la structure.
2. Implémenter `local_slope(grid, pos, move)` puis `greedy_descent(grid, start)`.
3. Tester plusieurs départs (bord, sommet) et commenter les chemins obtenus.

## 🧪 Variantes / exercices

- Empêcher les sorties de grille en bornant les indices (min/max).
- Limiter le nombre de pas pour simuler la fatigue d'un randonneur.
- Exporter la trajectoire finale dans un simple fichier texte (liste de coordonnées).

## 🔁 Séquence d'apprentissage progressive

1. Chargez la grille dans une liste de listes et inspectez les altitudes extrêmes.
2. Testez `local_slope` manuellement sur deux positions voisines pour valider les signes.
3. Appliquez `greedy_descent` sur plusieurs départs et notez les différences de trajectoire.

## 🧩 Snippets à compléter

```python
import csv

def load_grid(path):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        return [[float(cell) for cell in row] for row in reader]

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1),
         (-1, -1), (-1, 1), (1, -1), (1, 1)]

def local_slope(grid, pos, move):
    i, j = pos
    di, dj = move
    ni, nj = i + di, j + dj
    # TODO: vérifier que ni/nj restent dans la grille
    # TODO: retourner grid[i][j] - grid[ni][nj]


def greedy_descent(grid, start):
    path = [start]
    current = start
    while True:
        best_move = None
        best_drop = 0
        for move in MOVES:
            drop = local_slope(grid, current, move)
            # TODO: garder le move avec la plus grande chute positive
        if best_move is None:
            break
        i, j = current
        di, dj = best_move
        current = (i + di, j + dj)
        path.append(current)
    return path
```

## ✅ Corrigé / Notebook

- [Notebook local](../../Fuji%20Shimoyama%20problem.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Fuji%20Shimoyama%20problem.ipynb)
