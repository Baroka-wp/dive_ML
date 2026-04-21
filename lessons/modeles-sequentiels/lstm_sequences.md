# Explorer les cellules LSTM

_On dissèque les portes input/forget/output pour voir comment un LSTM retient (ou oublie) une information._

## 🎯 Objectifs
- Coder (ou au moins inspecter) les équations internes d'une cellule LSTM.
- Tester plusieurs longueurs de séquence et observer les gradients.
- **Prérequis bibliothèques** : TensorFlow/Keras ou PyTorch, NumPy.

## 🪜 Séquence d'apprentissage progressive
1. Définir un dataset séquentiel (prédire le prochain caractère/motif).
2. Configurer `tf.keras.layers.LSTM` et visualiser `state_h`, `state_c`.
3. Mettre en place un early stopping pour éviter le surapprentissage.

## 🧩 Snippets à compléter
```python
import tensorflow as tf

lstm = tf.keras.layers.LSTM(64, return_sequences=True, return_state=True)
outputs, h, c = lstm(tf.random.normal((1, 10, 8)))
# TODO: analyser les dimensions et interpréter h, c
```

## 🔁 Variantes / exercices
- Remplacer LSTM par GRU et comparer le nombre de paramètres.
- Appliquer le modèle à une série météo réelle (températures quotidiennes).
- Créer un notebook interactif où l'on trace `state_c` au fil des pas.

## 🔗 Ressources
- [Notebook local](../../LSTM.ipynb) – LSTM.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/LSTM.ipynb)
