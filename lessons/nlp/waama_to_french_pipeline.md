# Pipeline de traduction Waama → Français

_On prépare un corpus bilingue, on aligne les phrases et on crée des couples source/cible propres._

## 🎯 Objectifs
- Nettoyer les textes (accents, ponctuation) dans deux langues différentes.
- Construire des dictionnaires (token → index) synchronisés.
- **Prérequis bibliothèques** : pandas, NumPy, éventuellement spaCy/NLTK.

## 🪜 Séquence d'apprentissage progressive
1. Importer les deux colonnes (waama, français) et supprimer les doublons/phrases vides.
2. Tokeniser ligne par ligne puis aligner les longueurs via padding.
3. Sauvegarder les couples prêts à être utilisés dans un modèle Seq2Seq.

## 🧩 Snippets à compléter
```python
import pandas as pd

df = pd.read_csv("waama_french.csv")
df = df.dropna(subset=["waama", "french"])

def build_vocab(texts, min_freq=2):
    # TODO: créer un dictionnaire mot -> index
    return {"<pad>": 0, "<sos>": 1, "<eos>": 2}
```

## 🔁 Variantes / exercices
- Créer un jeu de validation en séparant 10% des paires.
- Ajouter des balises spéciales (<sos>, <eos>) pour guider le modèle.
- Analyser les phrases les plus longues et voir comment les découper.

## 🔗 Ressources
- [Notebook local](../../waama_to_french.ipynb) – waama_to_french.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/waama_to_french.ipynb)
