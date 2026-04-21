# Puissances & visualisation – Problème de pliage du papier

_Générer des épaisseurs après N pliages avec des boucles Python pures, puis préparer les données pour une éventuelle visualisation._

## 🎯 Objectifs pédagogiques

- Comparer approche `**` vs. boucle pour générer la même série d'épaisseurs.
- Mesurer les différences conceptuelles (lisibilité, performance) sans dépendre d'outils externes.
- Stocker les résultats dans une liste afin de pouvoir les exploiter (affichage console, sauvegarde).

## 🧱 Déroulé suggéré

1. Écrire `fold_series` avec une boucle et vérifier la sortie pour quelques pliages.
2. Ajouter une version utilisant `pow`/`**` et comparer les résultats.
3. Former un tableau texte (index, épaisseur) pour discussion ou copie dans un tableur.

## 🧪 Variantes / exercices

- Ajouter un paramètre `unit` pour afficher l'épaisseur en mm/cm/m.
- Générer automatiquement un fichier texte listant les valeurs.
- Créer une version inverse : déterminer le nombre de pliages pour atteindre une épaisseur cible.

## 🔁 Séquence d'apprentissage progressive

1. Implémentez la boucle de base et affichez la liste.
2. Ajoutez une vérification avec `pow` pour confirmer la cohérence.
3. Transformez la liste en texte formaté (tableau) ou fichier.

## 🧩 Snippets à compléter

```python
def fold_series(n_folds, thickness_mm=0.1):
    values = []
    current = thickness_mm
    for _ in range(n_folds + 1):
        values.append(current)
        # TODO: mettre à jour current pour le pliage suivant
    return values

series = fold_series(10)
for index, value in enumerate(series):
    print(index, value)
```

## ✅ Corrigé / Notebook

- [Notebook local](../../Probl%C3%A8me%20de%20pliage%20du%20papier.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Probl%C3%A8me%20de%20pliage%20du%20papier.ipynb)
