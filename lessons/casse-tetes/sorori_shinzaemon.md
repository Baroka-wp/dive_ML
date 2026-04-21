# Progression géométrique & besoins humains – Sorori Shinzaemon

_Simulation du nombre de grains de riz reçus chaque jour (doublement), conversion en grammes/calories et estimation du nombre de personnes/jours nourris._

## 🎯 Objectifs pédagogiques

- Programmer la suite 2^n et stocker les valeurs utiles dans un tableau Python/NumPy.
- Rechercher et justifier les hypothèses nutritionnelles (grammes → calories → besoins journaliers).
- Généraliser via une fonction bonus qui retourne combien de personnes peuvent survivre.

## 🧱 Déroulé suggéré

1. Calculer le nombre de grains au jour 100 et afficher la courbe cumulative.
2. Convertir en masse, en calories puis en nombre de repas par personne.
3. Implémenter la fonction bonus pour varier le jour ou le besoin énergétique.

## 🧪 Variantes / exercices

- Paramétrer les besoins énergétiques par profil (enfant, adulte, sportif).
- Visualiser la répartition des grains sur 100 jours (bar plot ou area chart).
- Utiliser `decimal` pour éviter les dépassements au-delà de 200 jours.

## 🔁 Séquence d'apprentissage progressive

1. Construire la liste des gains quotidiens (suite géométrique) et vérifier les premiers jours.
2. Convertir en grammes puis en calories à l'aide des hypothèses nutritionnelles documentées.
3. Implémenter une fonction qui estime le nombre de personnes/jours nourris pour un jour donné.
## 🧩 Snippets à compléter

```python
import math

def rice_per_day(days=100):
    grains = [2 ** d for d in range(1, days + 1)]
    return grains

def people_supported(day, need_per_person=94033):
    grains = rice_per_day(day)[-1]
    # TODO: convertir grains en nombre de personnes possibles
    # TODO: retourner le résultat (personnes, jours)

print(people_supported(100))
```
## ✅ Corrigé / Notebook

- [Notebook local](../../Sorori%20Shinzaemon%20problem.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Sorori%20Shinzaemon%20problem.ipynb)
