# Bag-of-Words et représentations de texte

_On code une version simplifiée du sac de mots pour transformer des phrases en vecteurs exploitables._

## 🎯 Objectifs
- Nettoyer un corpus (minuscules, stopwords) avant vectorisation.
- Construire un vocabulaire et calculer TF ou TF-IDF maison.
- **Prérequis bibliothèques** : Python, NumPy, pandas, éventuellement scikit-learn pour comparaison.

## 🪜 Séquence d'apprentissage progressive
1. Charger les textes bruts et appliquer un pipeline de nettoyage.
2. Compter les occurrences par document et remplir une matrice sparse.
3. Entraîner un classifieur simple (Naive Bayes, LogisticRegression) sur ces vecteurs.

## 🧩 Snippets à compléter
```python
import re
from collections import Counter

def tokenize(text):
    text = text.lower()
    tokens = re.findall(r"[a-zéèàùç]+", text)
    # TODO: retirer les stopwords
    return tokens

def bow_vector(tokens, vocab):
    counts = Counter(tokens)
    return [counts.get(word, 0) for word in vocab]
```

## 🔁 Variantes / exercices
- Basculer sur TF-IDF et observer l'effet sur les mots rares.
- Ajouter des n-grammes (bi-grammes) dans le vocabulaire.
- Comparer ton implémentation avec `sklearn.feature_extraction.text.CountVectorizer`.

## 🔗 Ressources
- [Notebook local](../../Traitement_du_langage_naturel.ipynb) – Traitement_du_langage_naturel.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Traitement_du_langage_naturel.ipynb)
