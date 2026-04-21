# Puissances & visualisation – Problème de pliage du papier

_Plusieurs méthodes pour calculer l'épaisseur après N pliages : opérateur de puissance, boucle, comparaison de temps, sauvegarde en liste et graphiques personnalisés._

## 🎯 Objectifs pédagogiques

- Réviser l'opérateur puissance, les conversions d'unités et le timing de code.
- Comparer approche itérative vs. exponentielle et mesurer leurs performances.
- Mettre en forme les données (listes, graphiques, personnalisation Matplotlib).

## 🧱 Déroulé suggéré

1. Implémenter les calculs avec `**` puis avec une boucle `for` pour ressentir la différence.
2. Utiliser `%timeit` pour comparer les temps et stocker les résultats dans une liste.
3. Tracer la progression (line plot) et proposer des options de personnalisation (titre, couleur).

## 🧪 Variantes / exercices

- Vectoriser avec NumPy pour générer l'épaisseur de 0 à N pliages en un appel.
- Ajouter un paramètre d'unité (mm/cm/m) et automatiser la conversion.
- Sauvegarder les résultats dans un CSV pour pouvoir les importer dans un tableur.

## 🔁 Séquence d'apprentissage progressive

1. Comparer l'utilisation de `**` et d'une boucle pour générer la même série d'épaisseurs.
2. Mesurer les temps d'exécution (`%timeit`) et discuter des compromis lisibilité/performance.
3. Transformer les résultats en visualisation (line plot) et sauvegarder les valeurs dans une liste.
## 🧩 Snippets à compléter

```python
def fold_series(n_folds, thickness_mm=0.1):
    values = []
    current = thickness_mm
    for _ in range(n_folds + 1):
        values.append(current)
        # TODO: mettre à jour current pour représenter le pliage suivant
    return values

series = fold_series(10)
print(series)
```
## ✅ Corrigé / Notebook

- [Notebook local](../../Probl%C3%A8me%20de%20pliage%20du%20papier.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Probl%C3%A8me%20de%20pliage%20du%20papier.ipynb)
