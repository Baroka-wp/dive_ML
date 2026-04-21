# Découvrir TensorFlow bas niveau

_On explore les tenseurs, les opérations différentiables et on écrit une boucle d'entraînement custom._

## 🎯 Objectifs
- Créer des `tf.constant` / `tf.Variable` et jouer avec l'auto-différenciation.
- Utiliser `tf.GradientTape` pour calculer les gradients à la main.
- **Prérequis bibliothèques** : TensorFlow 2.x.

## 🪜 Séquence d'apprentissage progressive
1. Manipuler les opérations de base (add, matmul, reshape) pour comprendre les types.
2. Coder une perte simple et calculer les gradients via GradientTape.
3. Écrire une mini-boucle d'entraînement personnalisée (forward → loss → backward).

## 🧩 Snippets à compléter
```python
import tensorflow as tf

w = tf.Variable(tf.random.normal((2, 1)))
b = tf.Variable(tf.zeros((1,)))

def model(x):
    return tf.matmul(x, w) + b

def train_step(x, y, lr=0.1):
    with tf.GradientTape() as tape:
        preds = model(x)
        loss = tf.reduce_mean((preds - y)**2)
    # TODO: récupérer les gradients et mettre à jour w, b
```

## 🔁 Variantes / exercices
- Comparer la boucle custom avec `model.fit` pour comprendre ce que fait Keras en coulisse.
- Tracer l'évolution des gradients pour diagnostiquer vanishing/explosion.
- Expérimenter avec des opérations non différentiables et observer les limites.

## 🔗 Ressources
- [Notebook local](../../TensorFlow.ipynb) – TensorFlow.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/TensorFlow.ipynb)
