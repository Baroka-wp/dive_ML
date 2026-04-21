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

## ✅ Corrigé / Notebook

- [Notebook local](../../Fuji%20Shimoyama%20problem.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Fuji%20Shimoyama%20problem.ipynb)
