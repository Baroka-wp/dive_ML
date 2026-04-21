# Descente de montagne – Fuji Shimoyama

_À partir d'une grille d'altitudes, on calcule la pente locale, choisit la prochaine case à descendre et trace les trajectoires selon différents départs/hyperparamètres._

## 🎯 Objectifs pédagogiques

- Charger et afficher la topographie (heatmap ou contour plot).
- Programmer les fonctions `calculate_slope`, `decide_next_point` et la boucle de descente.
- Comparer plusieurs points de départ et visualiser les chemins/temps de descente.

## 🧱 Déroulé suggéré

1. Importer les données d'altitude et les visualiser pour repérer les zones raides.
2. Écrire les fonctions de pente et de décision, puis une routine de descente complète.
3. Expérimenter différents départs, pas max et hyperparamètres et superposer les trajectoires.

## 🧪 Variantes / exercices

- Tester une stratégie multi-pas (regarder deux coups en avance).
- Ajouter une contrainte de pas maximum en mètres et observer l'impact.
- Exporter chaque trajet en GeoJSON ou CSV pour exploitation externe.

## 🔁 Séquence d'apprentissage progressive

1. Charger la matrice d'altitudes et visualiser la topographie avant tout calcul.
2. Implémenter les fonctions `local_slope` et `next_step` puis tester la descente depuis un point unique.
3. Boucler sur plusieurs points de départ et comparer graphiquement les trajectoires obtenues.
## 🧩 Snippets à compléter

```python
import numpy as np

ELEVATION = np.loadtxt('mtfuji_data.csv', delimiter=',')

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1),
         (-1, -1), (-1, 1), (1, -1), (1, 1)]

def local_slope(grid, pos, move):
    i, j = pos
    di, dj = move
    ni, nj = i + di, j + dj
    # TODO: vérifier que (ni, nj) reste dans la grille
    # TODO: retourner la différence d'altitude grid[i, j] - grid[ni, nj]


def greedy_descent(grid, start):
    path = [start]
    current = start
    while True:
        # TODO: calculer la pente pour chaque mouvement
        # TODO: choisir le move avec la plus forte pente descendante
        # TODO: arrêter si aucune pente négative n'est disponible
        path.append(current)
    return path
```
## ✅ Corrigé / Notebook

- [Notebook local](../../Fuji%20Shimoyama%20problem.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Fuji%20Shimoyama%20problem.ipynb)
