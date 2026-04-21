# Logarithmes appliqués – Mt. Fuji paper folding

_Calcul du nombre de pliages nécessaires pour dépasser la hauteur du Mont Fuji, factorisation dans une fonction et estimation de la longueur de papier requise._

## 🎯 Objectifs pédagogiques

- Utiliser les logarithmes ou une boucle pour déterminer rapidement le nombre de doublements.
- Écrire une fonction générique (épaisseur initiale, hauteur cible) et comparer boucle vs. `math.log2`.
- Estimer la longueur de papier nécessaire et discuter des ordres de grandeur obtenus.

## 🧱 Déroulé suggéré

1. Implémenter la version itérative qui multiplie l'épaisseur par deux jusqu'à dépasser la cible.
2. Factoriser dans une fonction pour tester d'autres sommets ou épaisseurs.
3. Calculer la longueur totale de papier et visualiser la progression.

## 🧪 Variantes / exercices

- Autoriser un facteur de croissance différent (×1.8) et comparer aux résultats théoriques.
- Afficher un graphique semi-log de l'épaisseur en fonction du nombre de pliages.
- Créer un petit CLI qui prend la hauteur cible en entrée utilisateur.

## ✅ Corrigé / Notebook

- [Notebook local](../../Mt.%20Fuji%20paper%20folding%20probem.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Mt.%20Fuji%20paper%20folding%20probem.ipynb)
