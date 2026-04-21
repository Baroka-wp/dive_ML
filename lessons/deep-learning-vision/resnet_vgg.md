# Décortiquer ResNet et VGG

_On révise la structure des CNN profonds classiques et on apprend à faire du transfert de style/knowledge._

## 🎯 Objectifs
- Comparer architecture séquentielle (VGG) vs résiduelle (ResNet).
- Geler/dégeler des couches pour le transfert d'apprentissage.
- **Prérequis bibliothèques** : TensorFlow/Keras ou PyTorch, NumPy.

## 🪜 Séquence d'apprentissage progressive
1. Charger un modèle pré-entraîné et inspecter ses couches.
2. Ajouter un petit classifieur (Dense) adapté à un dataset maison.
3. Finetuner quelques couches et observer l'évolution de l'accuracy.

## 🧩 Snippets à compléter
```python
import tensorflow as tf

base_model = tf.keras.applications.ResNet50(include_top=False, pooling="avg")
base_model.trainable = False  # TODO: basculer sur True pour finetune
x = tf.keras.layers.Dense(128, activation="relu")(base_model.output)
outputs = tf.keras.layers.Dense(10, activation="softmax")(x)
model = tf.keras.Model(inputs=base_model.input, outputs=outputs)
```

## 🔁 Variantes / exercices
- Comparer la taille mémoire / temps d'exécution entre VGG16 et ResNet34.
- Insérer une couche BatchNorm supplémentaire pour stabiliser l'entraînement.
- Organiser un mini-tournoi : quel modèle généralise le mieux sur vos photos d'école ?

## 🔗 Ressources
- [Notebook local](../../ResNetVGG.ipynb) – ResNetVGG.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/ResNetVGG.ipynb)
