# Architecture Seq2Seq générique

_Encoder une séquence, la décoder pas à pas : on construit le squelette des traducteurs automatiques._

## 🎯 Objectifs
- Comprendre la notion de contexte compressé dans un vecteur fixe.
- Implémenter (ou paramétrer) un encodeur et un décodeur avec attention optionnelle.
- **Prérequis bibliothèques** : TensorFlow/Keras ou PyTorch.

## 🪜 Séquence d'apprentissage progressive
1. Préparer les données : tokenisation, padding, dictionnaires.
2. Coder / instancier l'encodeur (RNN) puis le décodeur avec teacher forcing.
3. Évaluer la qualité en comparant séquence cible et séquence générée.

## 🧩 Snippets à compléter
```python
import tensorflow as tf

encoder = tf.keras.layers.GRU(128, return_state=True)
decoder = tf.keras.layers.GRU(128, return_sequences=True, return_state=True)
# TODO: mettre en place l'attention et la couche Dense finale
```

## 🔁 Variantes / exercices
- Ajouter un mécanisme d'attention Bahdanau ou Luong.
- Tester l'inférence greedy vs beam search.
- Adapter la structure à un problème de résumé de texte.

## 🔗 Ressources
- [Notebook local](../../Seq2Seq.ipynb) – Seq2Seq.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Seq2Seq.ipynb)
