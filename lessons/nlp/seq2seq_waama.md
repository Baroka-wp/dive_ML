# Seq2Seq Waama ↔ Français

_On entraîne (ou teste) un modèle encodeur-décodeur qui traduit automatiquement entre deux langues peu documentées._

## 🎯 Objectifs
- Mettre en place l'entraînement (teacher forcing, attention éventuelle).
- Évaluer la qualité de traduction avec des métriques simples (BLEU, exact match).
- **Prérequis bibliothèques** : TensorFlow/Keras ou PyTorch, NumPy.

## 🪜 Séquence d'apprentissage progressive
1. Charger les couples tokenisés depuis la leçon précédente.
2. Configurer l'encodeur/décodeur et suivre la perte sur train/validation.
3. Tester l'inférence (greedy ou beam search) puis analyser les erreurs.

## 🧩 Snippets à compléter
```python
import tensorflow as tf

encoder = tf.keras.layers.LSTM(128, return_sequences=False, return_state=True)
decoder = tf.keras.layers.LSTM(128, return_sequences=True, return_state=True)

def translate(sample):
    # TODO: encoder la phrase Waama, décoder token par token côté français
    return ""
```

## 🔁 Variantes / exercices
- Ajouter un mécanisme d'attention pour mieux gérer les phrases longues.
- Tester l'inversion (Français → Waama) et comparer les scores.
- Créer un glossaire illustré pour les mots que le modèle confond.

## 🔗 Ressources
- [Notebook local](../../seq2seq_waama.ipynb) – seq2seq_waama.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/seq2seq_waama.ipynb)
