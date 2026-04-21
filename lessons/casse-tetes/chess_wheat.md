# Suite géométrique – Problème de blé et d'échiquier

_Reconstitution de la légende du blé doublé sur chaque case : calcul pour 2×2 puis n×m, totalisation, heatmap et comparaison de méthodes (boucle, `np.append`, broadcast)._

## 🎯 Objectifs pédagogiques

- Programmer la progression 1, 2, 4… sur une grille et calculer le total de grains.
- Mettre en avant les gains de performance en vectorisant avec NumPy.
- Visualiser la distribution (heatmap log) et interpréter les régions dominantes.

## 🧱 Déroulé suggéré

1. Commencer par un échiquier 2×2 pour expliquer la règle, puis généraliser à n×m.
2. Comparer trois méthodes de génération et mesurer les temps CPU.
3. Tracer une heatmap et répondre aux questions 'combien de grains sur la seconde moitié ?'.

## 🧪 Variantes / exercices

- Introduire une règle alternative (triple sur les colonnes impaires) et comparer.
- Ajouter une fonction qui renvoie la case où un seuil de grains est franchi.
- Exporter les résultats sous forme de CSV/tableau pour insertion dans un support de cours.

## ✅ Corrigé / Notebook

- [Notebook local](../../Probl%C3%A8me%20de%20bl%C3%A9%20et%20d%27%C3%A9chiquier.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/Probl%C3%A8me%20de%20bl%C3%A9%20et%20d%27%C3%A9chiquier.ipynb)
