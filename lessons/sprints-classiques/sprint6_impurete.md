# Sprint 6 – Mesurer l'impureté d'un nœud

_On construit des fonctions pour calculer Gini ou entropie et piloter les splits d'un arbre de décision._

## 🎯 Objectifs
- Programmer des métriques d'impureté à partir de comptages de classes.
- Comprendre comment ces métriques guident la création des branches.
- **Prérequis bibliothèques** : NumPy, pandas, éventuellement scikit-learn pour vérifier.

## 🪜 Séquence d'apprentissage progressive
1. Écrire `gini(counts)` et `entropy(counts)` à partir de listes.
2. Parcourir plusieurs seuils pour choisir le split le plus pur.
3. Comparer l'arbre maison avec `DecisionTreeClassifier`.

## 🧩 Snippets à compléter
```python
import numpy as np

def gini(counts):
    total = counts.sum()
    # TODO: calculer 1 - sum((n/total)**2)
    return 0

def best_split(feature, target):
    # TODO: trier les valeurs, tester des coupures, retourner la meilleure
    pass
```

## 🔁 Variantes / exercices
- Visualiser l'évolution de l'impureté en fonction du seuil avec un graphe.
- Coder un critère custom (par exemple, gain minimum exigé).
- Comparer à l'entropie pour comprendre les différences pratiques.

## 🔗 Ressources
- [Notebook local](../../sprint6.ipynb) – sprint6.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/sprint6.ipynb)
