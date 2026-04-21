# Croissance exponentielle – Chestnut buns

_Modélisation d'un volume qui double toutes les cinq minutes jusqu'à couvrir un volume cible colossal (maison, planète, système solaire)._

## 🎯 Objectifs pédagogiques

- Traduire un énoncé exponentiel en fonction Python paramétrable (volume initial, pas de temps, volume cible).
- Stocker et tracer l'historique des volumes via Matplotlib pour visualiser la croissance explosive.
- Comparer différentes cibles en changeant les ordres de grandeur (lambda, maison, système solaire).

## 🧱 Déroulé suggéré

1. Coder la fonction `how_long_will_it_take_to_cover` en rendant le volume initial et l'intervalle configurables.
2. Créer un tableau des volumes successifs puis afficher la courbe volume vs. temps.
3. Analyser le résultat (minutes nécessaires, limites de la croissance exponentielle).

## 🧪 Variantes / exercices

- Ajouter un argument `growth_factor` pour simuler une croissance non parfaite (ex: ×1.8).
- Tracer simultanément plusieurs scénarios (maison, ville, planète) pour comparer les délais.
- Résoudre le problème inverse : combien de doublements restants pour atteindre un objectif donné ?

## 🔁 Séquence d'apprentissage progressive

1. Explorez la signification physique d'un doublement toutes les Δ minutes et comparez-la à d'autres croissances (linéaire, quadratique).
2. Paramétrez la fonction de simulation avec des volumes cibles variés (pièce, immeuble, planète) pour sentir les ordres de grandeur.
3. Interprétez la courbe volume vs. temps : discutez pourquoi la phase initiale paraît plate sur une échelle linéaire.
## 🧩 Snippets à compléter

```python
def simulate_growth(initial_volume, target_volume, factor=2, dt_minutes=5):
    volume = initial_volume
    timeline = [volume]
    minutes = 0
    while volume < target_volume:
        # TODO: incrémenter le temps de dt_minutes
        # TODO: multiplier le volume par le facteur de croissance
        # TODO: mémoriser le nouveau volume dans timeline
    return minutes, timeline

minutes_needed, history = simulate_growth(20, 1e9, factor=2, dt_minutes=5)
print(f"Objectif atteint en {minutes_needed} minutes")
```
## ✅ Corrigé / Notebook

- [Notebook local](../../%20%5BProblem%5D%20The%20day%20when%20chestnut%20buns%20cover%20the%20solar%20system.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/%20%5BProblem%5D%20The%20day%20when%20chestnut%20buns%20cover%20the%20solar%20system.ipynb)
