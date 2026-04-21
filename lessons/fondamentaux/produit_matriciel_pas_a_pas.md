# Comprendre le produit matriciel à la main

_On code soi-même l'opération clé des réseaux de neurones : multiplier deux matrices sans magie noire._

## 🎯 Objectifs
- Implémenter une fonction `matmul` avec des boucles imbriquées et vérifier les dimensions.
- Comparer son résultat à `numpy.dot` pour valider l'algorithme.
- **Prérequis bibliothèques** : Python (NumPy uniquement pour vérifier).

## 🪜 Séquence d'apprentissage progressive
1. Revoir la règle lignes × colonnes avec un schéma et un exemple 2×2.
2. Coder `matmul(a, b)` avec trois boucles et un accumulateur pour chaque case.
3. Générer des matrices aléatoires et écrire des tests automatisés simples.

## 🧩 Snippets à compléter
```python
def matmul(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    assert cols_a == rows_b, "Dimensions incompatibles"
    result = [[0 for _ in range(cols_b)] for __ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            s = 0
            for k in range(cols_a):
                # TODO: accumuler a[i][k] * b[k][j]
                pass
            result[i][j] = s
    return result
```

## 🔁 Variantes / exercices
- Compter le nombre d'opérations et relier cela au temps de calcul d'un réseau dense.
- Ajouter une option `transpose_second=True` pour manipuler directement `b.T`.
- Créer une version qui accepte des listes imbriquées **ou** des `numpy.ndarray`.

## 🔗 Ressources
- [Notebook local](../../Implementation%20of%20matrix%20product.ipynb) – Implementation of matrix product.ipynb
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Implementation%20of%20matrix%20product.ipynb)
