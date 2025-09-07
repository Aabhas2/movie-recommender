# 🎬 TMDB Movie Recommendation System

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.0+-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-0.24+-red.svg)
![NLTK](https://img.shields.io/badge/NLTK-3.6+-orange.svg)

> A sophisticated content-based movie recommendation system that leverages natural language processing and machine learning to suggest movies based on their content similarity.

## 📋 Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [Installation and Usage](#installation-and-usage)
- [Data Processing](#data-processing)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Dataset Description](#dataset-description)

## 🎯 Overview

This project implements an intelligent movie recommendation system using the TMDB 5000 Movie Dataset. By analyzing various aspects of movies including plot summaries, genres, keywords, cast, and crew information, the system provides personalized movie recommendations based on content similarity.

## ✨ Key Features

- **Multi-feature Analysis**: Incorporates multiple movie attributes for comprehensive similarity matching
  - Plot summaries and overviews
  - Genre classifications
  - Movie keywords and themes
  - Top 3 cast members
  - Director information

- **Advanced Text Processing**
  - Natural Language Processing (NLP) techniques
  - Text stemming and normalization
  - Stop word removal
  - Comprehensive text vectorization

- **Intelligent Similarity Matching**
  - Cosine similarity-based recommendations
  - Content-based filtering
  - Feature importance weighting

## 🛠️ Technology Stack

### Core Technologies
- **Python** (3.7+): Primary programming language
- **Jupyter Notebook**: Development environment

### Key Libraries
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **scikit-learn**: Machine learning operations
  - CountVectorizer: Text feature extraction
  - Cosine Similarity: Similarity calculations
- **NLTK**: Natural Language Processing
  - Porter Stemmer: Word stemming
  - Text preprocessing
- **ast**: Safe evaluation of string literals

## 🏗️ System Architecture

### Data Pipeline
1. **Data Ingestion**
   - Loading movie and credits datasets
   - Data validation and initial cleaning

2. **Feature Engineering**
   ```python
   # Example of feature extraction
   def convert(obj):
       L = []
       for i in ast.literal_eval(obj):
           L.append(i['name'])
       return L
   ```

3. **Text Processing**
   - Tokenization
   - Stemming
   - Stop word removal
   - Text normalization

4. **Vectorization**
   - Text to vector conversion
   - Feature space dimensionality: 5000
   - Sparse matrix representation

5. **Similarity Computation**
   - Cosine similarity matrix
   - Movie-to-movie similarity scores

## 🚀 Installation and Usage

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd recommender
   ```

2. Install required dependencies:
   ```bash
   pip install pandas numpy scikit-learn nltk
   ```

3. Download the TMDB dataset and place in the data directory:
   - Place `tmdb_5000_movies.csv` in `data/`
   - Place `tmdb_5000_credits.csv` in `data/`

4. Run the Jupyter notebook:
   ```bash
   jupyter notebook movie-recommender-system.ipynb
   ```

## 🔄 Data Processing

### Data Cleaning
- Handling missing values
- Removing duplicates
- Parsing nested JSON structures
- Text normalization

### Feature Engineering
1. **Text Features**
   - Overview text processing
   - Keyword extraction
   - Genre normalization

2. **Categorical Features**
   - Cast information extraction
   - Crew data processing
   - Genre encoding

3. **Combined Features**
   - Tag generation
   - Feature concatenation
   - Vector space transformation

## 🎯 How It Works

1. **Data Preparation**
   - Loads and merges movie data
   - Extracts relevant features
   - Processes text data

2. **Feature Processing**
   - Combines all features into tags
   - Applies text preprocessing
   - Creates numerical vectors

3. **Similarity Calculation**
   - Computes cosine similarity
   - Creates similarity matrix
   - Ranks similar movies

4. **Recommendation Generation**
   - Takes a movie input
   - Finds similar movies
   - Returns top recommendations

## 📁 Project Structure

```
recommender/
│
├── data/                      # Dataset directory
│   ├── tmdb_5000_movies.csv  # Movie information
│   └── tmdb_5000_credits.csv # Cast and crew data
│
├── movie-recommender-system.ipynb  # Main notebook
└── README.md                       # Documentation
```

## 📊 Dataset Description

The project utilizes the TMDB 5000 Movie Dataset, which includes:

### Movies Dataset (tmdb_5000_movies.csv)
- Movie titles and overviews
- Release dates
- Budget and revenue
- Genres and keywords
- Production companies

### Credits Dataset (tmdb_5000_credits.csv)
- Cast information
- Crew details
- Character names
- Department and job titles

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*Built with ❤️ for movie enthusiasts and data science practitioners*
