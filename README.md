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

<!-- BEGIN NOTEBOOK TOC -->
### 📑 Table des notebooks

- [ [Problem] The day when chestnut buns cover the solar system](./ [Problem] The day when chestnut buns cover the solar system.ipynb)
- [Analysis of housing information](./Analysis of housing information.ipynb)
- [anchored box02](./anchored_box02.ipynb)
- [Binary classification of iris](./Binary classification of iris.ipynb)
- [Creating dummy data](./Creating dummy data.ipynb)
- [creation de donnees](./creation_de_donnees.ipynb)
- [Credit information analysis](./Credit information analysis.ipynb)
- [Credit information learning](./Credit information learning.ipynb)
- [Darts throwing problem](./Darts throwing problem.ipynb)
- [Data analysis of iris](./Data analysis of iris.ipynb)
- [Data cleaning with python pandas](./Data cleaning with python pandas.ipynb)
- [Ecriture et Comprehension](./Ecriture_et_Comprehension.ipynb)
- [Faster R CNN and YOLO v3](./Faster_R_CNN_and_YOLO_v3.ipynb)
- [first colab](./first_colab.ipynb)
- [first notebook](./first_notebook.ipynb)
- [Fuji Shimoyama problem](./Fuji Shimoyama problem.ipynb)
- [Home Price Forecast](./Home Price Forecast.ipynb)
- [Implementation of matrix product](./Implementation of matrix product.ipynb)
- [keras](./keras.ipynb)
- [LSTM](./LSTM.ipynb)
- [Mt. Fuji paper folding probem](./Mt. Fuji paper folding probem.ipynb)
- [NumPy serie](./NumPy_serie.ipynb)
- [Problème de blé et d'échiquier](./Problème de blé et d'échiquier.ipynb)
- [Problème de pliage du papier](./Problème de pliage du papier.ipynb)
- [ResNetVGG](./ResNetVGG.ipynb)
- [Réseau de neurones récurrent (RNN) ](./Réseau_de_neurones_récurrent_(RNN)_.ipynb)
- [Seq2Seq](./Seq2Seq.ipynb)
- [seq2seq waama](./seq2seq_waama.ipynb)
- [SimpleConv1d](./SimpleConv1d.ipynb)
- [SimpleConv2d](./SimpleConv2d.ipynb)
- [Sorori Shinzaemon problem](./Sorori Shinzaemon problem.ipynb)
- [Sprint1-Flux d'apprentissage automatique](./Sprint1-Flux d'apprentissage automatique.ipynb)
- [Sprint10 Deep neuronal network](./Sprint10_Deep_neuronal_network.ipynb)
- [Sprint2 Introduction à l'apprentissage automatique scratch](./Sprint2 Introduction à l'apprentissage automatique scratch.ipynb)
- [Sprint3 Regression lineaire](./Sprint3_Regression_lineaire.ipynb)
- [Sprint4 Regression Logistique](./Sprint4_Regression_Logistique.ipynb)
- [Sprint5 SVM](./Sprint5_SVM.ipynb)
- [sprint6](./sprint6.ipynb)
- [Sprint7](./Sprint7.ipynb)
- [Sprint8 apprentissage d'ensemble](./Sprint8_apprentissage_d'ensemble.ipynb)
- [Sprint9 Neural network](./Sprint9_Neural_network.ipynb)
- [TensorFlow](./TensorFlow.ipynb)
- [Training data manipulation](./Training_data_manipulation.ipynb)
- [Traitement du langage naturel](./Traitement_du_langage_naturel.ipynb)
- [TURING CHALLENG](./TURING CHALLENG.ipynb)
- [Two-dimensional array and gradient problem](./Two-dimensional array and gradient problem.ipynb)
- [U net](./U_net.ipynb)
- [Utilization of object orientation](./Utilization of object orientation.ipynb)
- [waama to french](./waama_to_french.ipynb)

*Généré via `python scripts/generate_notebook_toc.py`.*
<!-- END NOTEBOOK TOC -->
