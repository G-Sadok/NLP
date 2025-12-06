# 🗣️ NLP Project: Text Analysis & Topic Modeling

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![NLTK](https://img.shields.io/badge/NLTK-Processing-green?style=for-the-badge&logo=python&logoColor=white)
![Gensim](https://img.shields.io/badge/Gensim-Topic_Modeling-orange?style=for-the-badge&logo=python&logoColor=white)
![WordCloud](https://img.shields.io/badge/WordCloud-Visualization-yellow?style=for-the-badge&logo=python&logoColor=white)

## 📖 Aperçu du Projet

Ce projet est une application pratique des techniques de **Traitement du Langage Naturel (NLP)**. Il vise à transformer des données textuelles brutes en *insights* visuels et thématiques.

Le projet est structuré de manière modulaire : une librairie de fonctions personnalisée alimente deux notebooks d'analyse distincts pour la visualisation (Nuage de mots) et la détection de sujets (Topic Modeling).

## 📂 Architecture du Code

Le projet sépare la logique de traitement (backend) de l'analyse exploratoire (frontend/notebooks) :

* **`nltk_functions.py`** : Le cœur du projet. Ce script contient toutes les fonctions réutilisables pour le pipeline de pré-traitement (tokenization, nettoyage, lemmatisation).
* **`word_cloud.ipynb`** : Notebook dédié à la visualisation de la fréquence des mots.
* **`topic_modeling.ipynb`** : Notebook dédié à la découverte de thèmes latents (LDA).
* **`My_stopwords.txt`** : Liste personnalisée de mots vides (stopwords) pour affiner le nettoyage spécifique au domaine.

## 🛠️ Pipeline de Pré-traitement (`nltk_functions.py`)

Le module `nltk_functions.py` implémente un pipeline complet de nettoyage de texte utilisant la librairie **NLTK** :

1.  **Nettoyage de base :** Conversion en minuscules et suppression de la ponctuation (Regex).
2.  **Tokenization :** Découpage du texte en mots individuels (`nltk.word_tokenize`).
3.  **Filtrage des Stopwords :** Suppression des mots courants sans valeur sémantique, en combinant la liste standard NLTK et le fichier `My_stopwords.txt`.
4.  **Normalisation :**
    * **Lemmatisation :** Réduction des mots à leur forme canonique (ex: "running" -> "run") via `WordNetLemmatizer`.
    * **Stemming :** Réduction des mots à leur racine via `PorterStemmer`.

## 📊 Analyses et Fonctionnalités

### 1. Visualisation par Nuage de Mots (`word_cloud.ipynb`)
Génération de **Word Clouds** pour identifier visuellement les termes les plus fréquents dans le corpus.
* Importation dynamique du module `nltk_functions` pour nettoyer le texte à la volée.
* Exportation du résultat en format interactif ou image (`wordcloud.html`).



[Image of Word Cloud example]


### 2. Modélisation de Sujets (`topic_modeling.ipynb`)
Utilisation d'algorithmes non supervisés pour extraire les thèmes principaux du corpus.
* **Technique :** LDA (Latent Dirichlet Allocation).
* **Vectorisation :** Transformation du texte en vecteurs numériques (Bag of Words ou TF-IDF) avant modélisation.
* **Objectif :** Grouper les documents similaires et comprendre de quoi parle le texte sans le lire intégralement.

## 🚀 Installation et Utilisation

1.  **Cloner le dépôt :**
    ```bash
    git clone [https://github.com/ton-user/nlp-analysis.git](https://github.com/ton-user/nlp-analysis.git)
    cd nlp-analysis
    ```

2.  **Pré-requis :**
    Assurez-vous d'avoir les corpus NLTK nécessaires (stopwords, punkt, wordnet).
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    ```

3.  **Lancer les analyses :**
    * Pour voir les nuages de mots : `jupyter notebook word_cloud.ipynb`
    * Pour explorer les topics : `jupyter notebook topic_modeling.ipynb`

---

## 🇬🇧 English Summary

**Project:** NLP Pipeline for Text Analysis and Topic Modeling

**Goal:** Process raw text data to extract visual insights (Word Clouds) and hidden themes (Topic Modeling) using a modular Python architecture.

**Key Features:**
* **Modular Codebase:** Core logic (cleaning, tokenization, lemmatization) is encapsulated in `nltk_functions.py` for reusability.
* **Custom Preprocessing:** Pipeline includes Regex cleaning, Stopword removal (using `My_stopwords.txt`), and NLTK-based Lemmatization/Stemming.
* **Visualization:** Word Cloud generation in `word_cloud.ipynb`.
* **Topic Modeling:** LDA implementation in `topic_modeling.ipynb` to uncover latent topics in the document corpus.

**Tech Stack:** Python, NLTK, Gensim, Scikit-learn, WordCloud.
