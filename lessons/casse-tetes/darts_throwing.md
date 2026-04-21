# Probabilités discrètes – Darts throwing problem

_Simulation de lancers de fléchettes guidés par un lancer de dé, stockage des impacts dans un dictionnaire puis visualisation de la cible._

## 🎯 Objectifs pédagogiques

- Rappeler la différence entre distributions discrètes et continues et utiliser un dictionnaire de listes.
- Simuler des tirages aléatoires avec `random`/`numpy` et relier chaque numéro de dé à plusieurs tirs (x, y).
- Tracer les impacts et styliser une cible (limites, cercles) sous Matplotlib.

## 🧱 Déroulé suggéré

1. Introduire les dictionnaires Python (clés/valeurs) puis construire `dart_loc_dic`.
2. Simuler de nombreux lancers (boucle) et peupler le dictionnaire avec les coordonnées tirées.
3. Visualiser les tirs, ajouter un cercle unité et commenter la répartition obtenue.

## 🧪 Variantes / exercices

- Remplacer le dé par deux dés (somme) et observer la nouvelle distribution.
- Compter combien de tirs tombent dans chaque anneau de la cible et afficher un histogramme.
- Exporter les tirs dans un DataFrame pandas pour analyses ultérieures.

## ✅ Corrigé / Notebook

- [Notebook local](../../Darts%20throwing%20problem.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Darts%20throwing%20problem.ipynb)
