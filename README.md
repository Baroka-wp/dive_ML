# dive_ML

> Exploratoire de notebooks Colab couvrant l'ensemble d'un parcours d'apprentissage automatique : prétraitement des données, algorithmes classiques, deep learning, vision, NLP et études de cas Kaggle.

## 📚 Ce que contient ce dépôt

| Bloc | Objectif | Notebooks clés |
| --- | --- | --- |
| Parcours "Sprints" | Construire pas à pas les bases ML (théorie + implémentations from scratch) | `Sprint1-Flux d'apprentissage automatique.ipynb` → `Sprint10_Deep_neuronal_network.ipynb`, `sprint6.ipynb` |
| Data science & Kaggle | Nettoyer, explorer, modéliser puis soumettre (`house-prices`, Home Credit) | `Home Price Forecast.ipynb`, `Credit information analysis.ipynb`, `Training_data_manipulation.ipynb`, `house-prices/` |
| Vision & séries temporelles | CNN, U-Net, détection (YOLO/Faster R-CNN), LSTM/Seq2Seq | `ResNetVGG.ipynb`, `U_net.ipynb`, `Faster_R_CNN_and_YOLO_v3.ipynb`, `LSTM.ipynb`, `Seq2Seq.ipynb` |
| NLP & linguistique | Traitement automatique Waama↔Français, compréhension de textes | `Traitement_du_langage_naturel.ipynb`, `Ecriture_et_Comprehension.ipynb`, `waama_to_french.ipynb` |
| Casse-têtes et maths appliquées | Exercices sur Mt Fuji, Sorori Shinzaemon, probabilités, optimisation | `Sorori Shinzaemon problem.ipynb`, `Mt. Fuji paper folding problem.ipynb`, `Two-dimensional array and gradient problem.ipynb` |

Les dossiers CSV (`train.csv`, `test.csv`, `submission.csv`, `HomeCredit_columns_description.csv`, `property data.csv`, `mtfuji_data.csv`, etc.) servent de jeux pédagogiques. Le log `app.log` garde des traces d'exécutions locales.

## 🚀 Prise en main

1. **Cloner**
   ```bash
   git clone https://github.com/Baroka-wp/dive_ML.git
   cd dive_ML
   ```
2. **Environnement recommandé**
   - Python 3.10+
   - JupyterLab ou Google Colab
   - Packages usuels : `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `xgboost`, `lightgbm`, `tensorflow`/`keras`, `torch`, `opencv-python`, `spacy`, `nltk`, `plotly`.
   - Installe-les en bloc via :
     ```bash
     pip install -r requirements.txt  # (à générer selon vos besoins)
     ```
3. **Datasets volumineux**
   - Les CSV déjà versionnés suffisent pour la plupart des notebooks.
   - Pour d'autres concours Kaggle, ajoute les fichiers dans `data/` ou mets à jour les chemins en début de notebook.

## 🧭 Chemin d'apprentissage suggéré

1. **Sprints 1 → 6** : pipeline ML, régression, classification, SVM/KNN, validation croisée.
2. **Sprints 7 → 10** : réseaux neuronaux, optimisation et bonnes pratiques.
3. **Cas pratiques** : `Home Price Forecast`, `Credit information analysis`, `house-prices/`.
4. **Deep learning avancé** : `ResNetVGG`, `U_net`, `Faster_R_CNN_and_YOLO_v3`, `Seq2Seq`.
5. **NLP & bilinguisme** : `Traitement_du_langage_naturel`, `waama_to_french`.
6. **Math puzzles** : Mt Fuji, Sorori Shinzaemon, problèmes combinatoires.

## 🛠️ Bonnes pratiques

- **Versionner vos données générées** (modèles, checkpoints) dans un dossier `artifacts/` ignoré par git.
- **Documenter les dépendances** : créez un `requirements.txt` ou `environment.yml` par notebook si nécessaire.
- **Normaliser les chemins** en utilisant `Pathlib` et des variables `DATA_DIR` pour exécuter indifféremment en local ou sur Colab.
- **Ajouter des sorties clés** (tableaux de bord, métriques) en fin de notebook pour faciliter les revues.

## 🔜 Pistes d'amélioration

- Générer automatiquement une table des matières des notebooks.
- Fournir des scripts d'orchestration (`make`, `tox`, `nox`) pour rejouer les expériences critiques.
- Mettre en place des tests rapides (lint, unitaires) sur les fonctions utilitaires présentes dans certains notebooks.

---

Ce README est volontairement synthétique : il sert de porte d'entrée. Libre à toi de détailler chaque sprint, décrire les datasets ou ajouter des captures d'écran selon les besoins de la formation.
