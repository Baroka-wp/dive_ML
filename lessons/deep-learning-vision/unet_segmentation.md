# Segmenter des images avec U-Net

_On apprend à découper une image en zones (routes, rivages, cellules) grâce à une architecture en U._

## 🎯 Objectifs
- Préparer des masques pixellisés alignés sur les images originales.
- Configurer l'encodeur-décodeur et surveiller les métriques IoU/Dice.
- **Prérequis bibliothèques** : TensorFlow/Keras ou PyTorch, NumPy, OpenCV/Pillow.

## 🪜 Séquence d'apprentissage progressive
1. Créer un DataLoader qui retourne (image, masque) avec les mêmes dimensions.
2. Implémenter les blocs conv + upsampling caractéristiques d'U-Net.
3. Visualiser quelques prédictions pour vérifier la qualité du contour.

## 🧩 Snippets à compléter
```python
import tensorflow as tf

def unet_block(filters, name):
    return tf.keras.Sequential([
        tf.keras.layers.Conv2D(filters, 3, activation="relu", padding="same", name=f"{name}_conv1"),
        tf.keras.layers.Conv2D(filters, 3, activation="relu", padding="same", name=f"{name}_conv2")
    ])
# TODO: assembler encoder et decoder
```

## 🔁 Variantes / exercices
- Ajouter des skip connections customisées (attention gates).
- Tester la perte Dice vs BinaryCrossentropy.
- Mesurer l'impact de l'augmentation de données (flip, rotation).

## 🔗 Ressources
- [Notebook local](../../U_net.ipynb) – U_net.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/U_net.ipynb)
