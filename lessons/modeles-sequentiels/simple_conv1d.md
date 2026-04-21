# Convolutions 1D pour séries

_On utilise des filtres 1D pour repérer des motifs dans des signaux (audio, texte vectorisé, séries météo)._

## 🎯 Objectifs
- Coder une couche conv1d limitée puis la comparer à l'implémentation framework.
- Visualiser la sortie d'un filtre pour comprendre ce qu'il détecte.
- **Prérequis bibliothèques** : NumPy, éventuellement PyTorch/TensorFlow.

## 🪜 Séquence d'apprentissage progressive
1. Créer un signal synthétique (somme de sinus + bruit).
2. Appliquer une convolution glissante et interpréter la réponse.
3. Empiler plusieurs filtres pour détecter différents motifs.

## 🧩 Snippets à compléter
```python
import numpy as np

def conv1d(signal, kernel):
    output = np.zeros(len(signal) - len(kernel) + 1)
    for i in range(len(output)):
        window = signal[i:i+len(kernel)]
        # TODO: multiplication élément par élément puis somme
        output[i] = 0
    return output
```

## 🔁 Variantes / exercices
- Tester plusieurs noyaux (détecteur de pics, moyenne glissante).
- Comparer convolution manuelle vs `torch.nn.Conv1d`.
- Appliquer la couche sur des embeddings de mots pour repérer des bigrammes.

## 🔗 Ressources
- [Notebook local](../../SimpleConv1d.ipynb) – SimpleConv1d.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/SimpleConv1d.ipynb)
