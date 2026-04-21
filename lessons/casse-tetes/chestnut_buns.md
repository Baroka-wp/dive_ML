# Croissance exponentielle – Chestnut buns

_Modélisation 100% Python natif d'un volume qui double toutes les cinq minutes jusqu'à couvrir un volume cible colossal (maison, planète, système solaire)._ 

## 🎯 Objectifs pédagogiques

- Traduire un énoncé exponentiel en fonction Python pure (boucles, opérations sur entiers/flottants) sans dépendre de bibliothèques externes.
- Stocker l'historique dans des listes pour raisonner sur la croissance et, en option, préparer une visualisation ultérieure.
- Comparer différentes cibles en jouant uniquement sur les paramètres de la fonction.

## 🧱 Déroulé suggéré

1. Coder `how_long_will_it_take_to_cover` avec paramètres (volume initial, pas de temps, cible, facteur).
2. Créer un tableau des volumes successifs et imprimer quelques étapes clés pour sentir l'explosion.
3. Analyser le résultat (minutes nécessaires, nombre de doublements) et discuter des limites du modèle.

## 🧪 Variantes / exercices

- Ajouter un argument `growth_factor` pour simuler des croissances imparfaites (×1.8, ×2.5, etc.).
- Tracer simultanément plusieurs scénarios en affichant simplement les couples (temps, volume) dans la console.
- Résoudre le problème inverse : combien de doublements restants avant d'atteindre l'objectif ?

## 🔁 Séquence d'apprentissage progressive

1. Explorez la signification physique d'un doublement toutes les Δ minutes vs. une progression linéaire.
2. Paramétrez la fonction avec des volumes cibles variés (pièce, immeuble, planète) pour comparer les ordres de grandeur.
3. Interprétez les impressions (volume vs. temps) pour expliquer pourquoi la phase initiale semble plate.

## 🧩 Snippets à compléter

```python
def simulate_growth(initial_volume, target_volume, factor=2, dt_minutes=5):
    volume = initial_volume
    timeline = [(0, volume)]
    minutes = 0
    while volume < target_volume:
        # TODO: incrémenter minutes du pas dt_minutes
        # TODO: multiplier volume par le facteur de croissance
        # TODO: ajouter (minutes, volume) à timeline
    return minutes, timeline

minutes_needed, history = simulate_growth(20, 1_000_000)
print(f"Objectif atteint en {minutes_needed} minutes")
```

## ✅ Corrigé / Notebook

- [Notebook local](../../%20%5BProblem%5D%20The%20day%20when%20chestnut%20buns%20cover%20the%20solar%20system.ipynb)
- [Ouvrir dans Colab](https://colab.research.google.com/github/Baroka-wp/dive_ML/blob/master/%20%5BProblem%5D%20The%20day%20when%20chestnut%20buns%20cover%20the%20solar%20system.ipynb)
