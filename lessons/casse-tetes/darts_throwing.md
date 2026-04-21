# Probabilités discrètes – Darts throwing problem

_Simulation de lancers de fléchettes entièrement en Python standard (`random`, listes, dictionnaires) pour explorer les distributions discrètes._

## 🎯 Objectifs pédagogiques

- Manipuler dictionnaires/listes pour enregistrer des évènements catégoriels sans bibliothèques externes.
- Utiliser le module `random` pour simuler des lancers et alimenter une structure de données.
- Interpréter les résultats sous forme de comptages (affichages console) avant de penser visualisation.

## 🧱 Déroulé suggéré

1. Revoir distributions discrètes vs continues et initialiser `dart_log = {face: [] ...}`.
2. Boucler sur `n` lancers, tirer un dé (`randint`) et des coordonnées (`uniform`), stocker celles qui tombent dans le cercle unité.
3. Compter les occurrences par face et commenter la répartition.

## 🧪 Variantes / exercices

- Remplacer le dé par deux dés (somme) et comparer la distribution finale.
- Compter combien de tirs tombent dans chaque anneau (rayon < 0.5, 0.5-1, etc.).
- Exporter les tirs sous forme de texte (`csv.writer`) pour exploitation ultérieure.

## 🔁 Séquence d'apprentissage progressive

1. Construisez un dictionnaire vide pour capturer les tirs par valeur de dé.
2. Programmez la boucle de simulation et affichez les premières entrées pour valider la structure.
3. Ajoutez un calcul de fréquences (pourcentage) et discutez de la convergence vers l'uniforme.

## 🧩 Snippets à compléter

```python
import random

def simulate_darts(n_throws=50):
    dart_log = {face: [] for face in range(1, 7)}
    for _ in range(n_throws):
        die = random.randint(1, 6)
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        # TODO: vérifier si x**2 + y**2 <= 1
        # TODO: si oui, ajouter (x, y) dans dart_log[die]
    return dart_log

results = simulate_darts(200)
print({face: len(hits) for face, hits in results.items()})
```

## ✅ Corrigé / Notebook

- [Notebook local](../../Darts%20throwing%20problem.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Darts%20throwing%20problem.ipynb)
