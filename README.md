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

0. **Préambule – Python / NumPy / pandas / Matplotlib** : `first_notebook.ipynb`, `NumPy_serie.ipynb`, `Training_data_manipulation.ipynb`, `Data cleaning with python pandas.ipynb`.
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

## 📘 Modules de cours – Casse-têtes & maths appliquées

Ces notes de cours proposent un déroulé pédagogique avec exercices et renvoient au notebook comme corrigé.

| Module | Notebook corrigé |
| --- | --- |
| [Croissance exponentielle – Chestnut buns](lessons/casse-tetes/chestnut_buns.md) | [Notebook](./%20%5BProblem%5D%20The%20day%20when%20chestnut%20buns%20cover%20the%20solar%20system.ipynb) |
| [Probabilités discrètes – Darts throwing problem](lessons/casse-tetes/darts_throwing.md) | [Notebook](./Darts%20throwing%20problem.ipynb) |
| [Descente de montagne – Fuji Shimoyama](lessons/casse-tetes/fuji_shimoyama.md) | [Notebook](./Fuji%20Shimoyama%20problem.ipynb) |
| [Logarithmes appliqués – Mt. Fuji paper folding](lessons/casse-tetes/mt_fuji_paper.md) | [Notebook](./Mt.%20Fuji%20paper%20folding%20probem.ipynb) |
| [Suite géométrique – Problème de blé et d'échiquier](lessons/casse-tetes/chess_wheat.md) | [Notebook](./Probl%C3%A8me%20de%20bl%C3%A9%20et%20d%27%C3%A9chiquier.ipynb) |
| [Puissances & visualisation – Problème de pliage du papier](lessons/casse-tetes/paper_folding.md) | [Notebook](./Probl%C3%A8me%20de%20pliage%20du%20papier.ipynb) |
| [Progression géométrique & besoins humains – Sorori Shinzaemon](lessons/casse-tetes/sorori_shinzaemon.md) | [Notebook](./Sorori%20Shinzaemon%20problem.ipynb) |


<!-- BEGIN NOTEBOOK TOC -->
### 📑 Table des notebooks (navigation thématique)

#### Fondamentaux Python / NumPy / Pandas

- [Creating dummy data](./Creating%20dummy%20data.ipynb)
- [creation de donnees](./creation_de_donnees.ipynb)
- [first colab](./first_colab.ipynb)
- [first notebook](./first_notebook.ipynb)
- [Implementation of matrix product](./Implementation%20of%20matrix%20product.ipynb)
- [NumPy serie](./NumPy_serie.ipynb)
- [seq2seq waama](./seq2seq_waama.ipynb)
- [Training data manipulation](./Training_data_manipulation.ipynb)
- [Two-dimensional array and gradient problem](./Two-dimensional%20array%20and%20gradient%20problem.ipynb)
- [Utilization of object orientation](./Utilization%20of%20object%20orientation.ipynb)
- [waama to french](./waama_to_french.ipynb)

#### Préparation de données & exploration tabulaire

- [Analysis of housing information](./Analysis%20of%20housing%20information.ipynb)
- [Credit information analysis](./Credit%20information%20analysis.ipynb)
- [Credit information learning](./Credit%20information%20learning.ipynb)
- [Data analysis of iris](./Data%20analysis%20of%20iris.ipynb)
- [Data cleaning with python pandas](./Data%20cleaning%20with%20python%20pandas.ipynb)
- [Home Price Forecast](./Home%20Price%20Forecast.ipynb)

#### Parcours Sprints & algorithmes classiques

- [Binary classification of iris](./Binary%20classification%20of%20iris.ipynb)
- [Sprint1-Flux d'apprentissage automatique](./Sprint1-Flux%20d%27apprentissage%20automatique.ipynb)
- [Sprint10 Deep neuronal network](./Sprint10_Deep_neuronal_network.ipynb)
- [Sprint2 Introduction à l'apprentissage automatique scratch](./Sprint2%20Introduction%20%C3%A0%20l%27apprentissage%20automatique%20scratch.ipynb)
- [Sprint3 Regression lineaire](./Sprint3_Regression_lineaire.ipynb)
- [Sprint4 Regression Logistique](./Sprint4_Regression_Logistique.ipynb)
- [Sprint5 SVM](./Sprint5_SVM.ipynb)
- [sprint6](./sprint6.ipynb)
- [Sprint7](./Sprint7.ipynb)
- [Sprint8 apprentissage d'ensemble](./Sprint8_apprentissage_d%27ensemble.ipynb)
- [Sprint9 Neural network](./Sprint9_Neural_network.ipynb)

#### Deep learning & vision

- [anchored box02](./anchored_box02.ipynb)
- [Faster R CNN and YOLO v3](./Faster_R_CNN_and_YOLO_v3.ipynb)
- [keras](./keras.ipynb)
- [ResNetVGG](./ResNetVGG.ipynb)
- [SimpleConv1d](./SimpleConv1d.ipynb)
- [SimpleConv2d](./SimpleConv2d.ipynb)
- [TensorFlow](./TensorFlow.ipynb)
- [TURING CHALLENG](./TURING%20CHALLENG.ipynb)
- [U net](./U_net.ipynb)

#### Modèles séquentiels & séries temporelles

- [LSTM](./LSTM.ipynb)
- [Réseau de neurones récurrent (RNN) ](./R%C3%A9seau_de_neurones_r%C3%A9current_%28RNN%29_.ipynb)
- [Seq2Seq](./Seq2Seq.ipynb)

#### NLP & compréhension

- [Ecriture et Comprehension](./Ecriture_et_Comprehension.ipynb)
- [Traitement du langage naturel](./Traitement_du_langage_naturel.ipynb)

#### Casse-têtes & mathématiques appliquées

- [ [Problem] The day when chestnut buns cover the solar system](./%20%5BProblem%5D%20The%20day%20when%20chestnut%20buns%20cover%20the%20solar%20system.ipynb)
- [Darts throwing problem](./Darts%20throwing%20problem.ipynb)
- [Fuji Shimoyama problem](./Fuji%20Shimoyama%20problem.ipynb)
- [Mt. Fuji paper folding probem](./Mt.%20Fuji%20paper%20folding%20probem.ipynb)
- [Problème de blé et d'échiquier](./Probl%C3%A8me%20de%20bl%C3%A9%20et%20d%27%C3%A9chiquier.ipynb)
- [Problème de pliage du papier](./Probl%C3%A8me%20de%20pliage%20du%20papier.ipynb)
- [Sorori Shinzaemon problem](./Sorori%20Shinzaemon%20problem.ipynb)

*Généré via `python scripts/generate_notebook_toc.py`.*
<!-- END NOTEBOOK TOC -->
