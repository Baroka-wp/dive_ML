# Ancrer des boîtes pour la détection

_On apprend à définir des ancres (anchor boxes) pour couvrir différentes tailles d'objets avant même l'entraînement._

## 🎯 Objectifs
- Comprendre comment générer une grille d'ancres à plusieurs ratios.
- Calculer IoU pour évaluer quelles ancres collent le mieux aux objets réels.
- **Prérequis bibliothèques** : NumPy, Matplotlib, éventuellement OpenCV.

## 🪜 Séquence d'apprentissage progressive
1. Générer un maillage (x, y) et des tailles de boîtes candidates.
2. Écrire une fonction `iou(box_a, box_b)` et la tester sur plusieurs exemples.
3. Visualiser les ancres retenues sur une image exemple.

## 🧩 Snippets à compléter
```python
import numpy as np

def generate_anchors(grid_size, ratios, scales):
    anchors = []
    # TODO: boucler sur chaque cellule et créer les boîtes
    return np.array(anchors)

def iou(box_a, box_b):
    # TODO: calculer l'intersection / union
    return 0.0
```

## 🔁 Variantes / exercices
- Tester différentes résolutions de grille et mesurer l'impact sur le rappel.
- Comparer la stratégie YOLO (cellule unique) vs Faster R-CNN (proposals multiples).
- Créer un mini-jeu : retrouver quel anchor correspond à quel objet sur une image d'école.

## 🔗 Ressources
- [Notebook local](../../anchored_box02.ipynb) – anchored_box02.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/anchored_box02.ipynb)
