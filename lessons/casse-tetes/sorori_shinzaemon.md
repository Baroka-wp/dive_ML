# Progression géométrique & besoins humains – Sorori Shinzaemon

_Modéliser le conte du riz doublé chaque jour uniquement avec les outils standards de Python._

## 🎯 Objectifs pédagogiques

- Programmer la suite 2^n et stocker les valeurs dans des listes Python.
- Convertir grains → grammes → calories sans bibliothèques externes.
- Implémenter une fonction générique pour estimer le nombre de personnes/jours nourris.

## 🧱 Déroulé suggéré

1. Construire la liste des gains quotidiens et vérifier les premiers jours.
2. Convertir en masse puis en calories via les hypothèses documentées.
3. Calculer combien de personnes peuvent être nourries et pendant combien de jours.

## 🧪 Variantes / exercices

- Paramétrer les besoins énergétiques selon le profil (enfant, adulte, sportif).
- Générer un affichage (texte) du nombre de grains par jour.
- Étendre la simulation au-delà de 100 jours et discuter des limitations numériques.

## 🔁 Séquence d'apprentissage progressive

1. Construisez `rice_per_day` et affichez les 5 premières valeurs.
2. Ajoutez la conversion en grammes/calories et expliquez vos hypothèses.
3. Implémentez `people_supported` et testez plusieurs jours.

## 🧩 Snippets à compléter

```python
def rice_per_day(days=100):
    grains = []
    current = 1
    for _ in range(days):
        current *= 2
        grains.append(current)
    return grains

def people_supported(day, need_per_person=94_033):
    grains = rice_per_day(day)[-1]
    # TODO: calculer le nombre de personnes possibles
    # TODO: retourner (personnes, jours)

print(people_supported(100))
```

## ✅ Corrigé / Notebook

- [Notebook local](../../Sorori%20Shinzaemon%20problem.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Sorori%20Shinzaemon%20problem.ipynb)
