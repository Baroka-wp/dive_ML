# Structurer son code avec des classes

_On transforme des fonctions dispersées en une mini-boîte à outils orientée objet pour mieux organiser ses expériences._

## 🎯 Objectifs
- Définir une classe avec `__init__`, attributs et méthodes claires.
- Réutiliser cette classe pour créer plusieurs instances (capteurs, expériences, joueurs…).
- **Prérequis bibliothèques** : Python standard.

## 🪜 Séquence d'apprentissage progressive
1. Lister les données à encapsuler (nom, mesures, unité).
2. Coder la classe avec une méthode `record` et une méthode `summary`.
3. Ajouter une méthode de classe ou statique pour créer des objets préconfigurés.

## 🧩 Snippets à compléter
```python
class SensorLog:
    def __init__(self, name, unit="°C"):
        self.name = name
        self.unit = unit
        self.readings = []

    def add_reading(self, value, minute):
        # TODO: stocker les mesures (minute, value)
        pass

    def summary(self):
        # TODO: retourner min / max / moyenne
        pass

room = SensorLog("Salle info")
room.add_reading(22.5, minute=0)
```

## 🔁 Variantes / exercices
- Ajouter une méthode `to_dataframe()` si pandas est disponible.
- Créer une sous-classe `OutdoorSensor` qui gère humidité + température.
- Brancher cette classe sur un notebook précédent pour enregistrer des expériences.

## 🔗 Ressources
- [Notebook local](../../Utilization%20of%20object%20orientation.ipynb) – Utilization of object orientation.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Utilization%20of%20object%20orientation.ipynb)
