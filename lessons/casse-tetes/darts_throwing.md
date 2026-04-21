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

## 🔁 Séquence d'apprentissage progressive

1. Revoir les types de distribution (discrète/continue) et créer un dictionnaire vide pour capturer les tirs par valeur de dé.
2. Programmer la boucle de simulation (n lancers) et remplir progressivement la structure `dart_log`.
3. Visualiser la cible en ajoutant cercles / quadrants puis commenter la densité observée.
## 🧩 Snippets à compléter

```python
import random

def simulate_darts(n_throws=50):
    dart_log = {face: [] for face in range(1, 7)}
    for _ in range(n_throws):
        die = random.randint(1, 6)
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        # TODO: vérifier si (x, y) est dans le cercle unité
        # TODO: si oui, ajouter les coordonnées à dart_log[die]
    return dart_log

results = simulate_darts(200)
print({face: len(hits) for face, hits in results.items()})
```
## ✅ Corrigé / Notebook

- [Notebook local](../../Darts%20throwing%20problem.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Darts%20throwing%20problem.ipynb)
