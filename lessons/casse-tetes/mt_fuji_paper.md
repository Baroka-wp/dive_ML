# Logarithmes appliqués – Mt. Fuji paper folding

_Déterminer le nombre de pliages avec un raisonnement purement Python (boucles + `math`)._

## 🎯 Objectifs pédagogiques

- Utiliser boucles et logarithmes (`math.log2`) pour estimer rapidement un nombre de doublements.
- Factoriser la résolution dans une fonction générique sans recourir à NumPy.
- Estimer la longueur de papier requise en manipulant seulement des nombres natifs.

## 🧱 Déroulé suggéré

1. Calculer quelques pliages à la main puis coder la boucle équivalente.
2. Comparer la boucle à la version analytique (logarithme) pour valider la cohérence.
3. Calculer la longueur de papier nécessaire et analyser l'ordre de grandeur.

## 🧪 Variantes / exercices

- Introduire un facteur de croissance différent (×1.8) et comparer aux résultats théoriques.
- Ajouter un paramètre pour choisir l'unité d'entrée (mm/cm/m).
- Générer un tableau (liste) des épaisseurs pour 0…N pliages et l'afficher proprement.

## 🔁 Séquence d'apprentissage progressive

1. Faites tourner la boucle sur une petite hauteur (1 mètre) pour suivre les valeurs.
2. Ajoutez le calcul analytique et comparez les résultats.
3. Généralisez la fonction pour accepter d'autres sommets ou épaisseurs.

## 🧩 Snippets à compléter

```python
import math

def folds_to_reach(height_m, thickness_mm=0.1):
    thickness_m = thickness_mm / 1000
    folds = 0
    current = thickness_m
    while current < height_m:
        # TODO: augmenter folds et doubler current
    analytical = math.ceil(math.log2(height_m / thickness_m))
    return folds, analytical

print(folds_to_reach(3776))
```

## ✅ Corrigé / Notebook

- [Notebook local](../../Mt.%20Fuji%20paper%20folding%20probem.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Mt.%20Fuji%20paper%20folding%20probem.ipynb)
