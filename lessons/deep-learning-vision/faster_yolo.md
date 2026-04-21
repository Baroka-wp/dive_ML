# Faster R-CNN et YOLO v3

_On compare deux familles de détecteurs modernes : région-proposal vs prédiction directe en une passe._

## 🎯 Objectifs
- Lire une carte de features et comprendre comment chaque modèle propose ses boîtes.
- Lancer un entraînement rapide et analyser la précision/recall obtenue.
- **Prérequis bibliothèques** : PyTorch ou TensorFlow, NumPy, OpenCV.

## 🪜 Séquence d'apprentissage progressive
1. Préparer les données (annotation JSON ou CSV) et normaliser les images.
2. Configurer un notebook pour entraîner YOLOv3 ou Faster R-CNN sur un échantillon réduit.
3. Comparer qualitativement les prédictions en superposant les boîtes.

## 🧩 Snippets à compléter
```python
import torch

def train_detector(model, dataloader, epochs=5):
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-4)
    for epoch in range(epochs):
        for images, targets in dataloader:
            # TODO: passer les images dans le modèle
            # TODO: calculer la loss (cls + bbox)
            # TODO: backprop + update
            pass
```

## 🔁 Variantes / exercices
- Changer la taille d'entrée (320 vs 608) et mesurer l'effet sur le FPS.
- Appliquer le modèle à des objets du quotidien (cartables, ballons).
- Créer un tableau comparatif YOLO vs Faster (latence, précision).

## 🔗 Ressources
- [Notebook local](../../Faster_R_CNN_and_YOLO_v3.ipynb) – Faster_R_CNN_and_YOLO_v3.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Faster_R_CNN_and_YOLO_v3.ipynb)
