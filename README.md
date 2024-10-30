# Iris-Flower-Classifier🌸
![51518iris img1](https://github.com/user-attachments/assets/c6f757d5-250e-4237-9e19-ebbd40a2c2b3)

## Overview
This project classifies iris flower species (Setosa, Versicolor, Virginica) using various classification models, including Logistic Regression, K-Nearest Neighbors (KNN), Support Vector Machine (SVM), and Naive Bayes. The models are trained on the Iris dataset and evaluated to determine the best-performing model.

## Live Demo
🔗 Take a look at my Iris flower classifier👉🏻 
[![Experience It! 🌟](https://img.shields.io/badge/Experience%20It!🌟-blue)](your-streamlit-link)

<br>

## Table of Contents
1. [Features](#features)
2. [Dataset](#dataset)
3. [Data Preprocessing](#data-preprocessing)
4. [Models](#models)
5. [Evaluation](#evaluation)
6. [Installation](#installation)
7. [Usage](#usage)
8. [Technologies Used](#technologies-used)
9. [Results](#results)
10. [Contact](#contact)

## Features
- Loads and cleans the Iris dataset
- Scales input features for consistent model performance
- Trains multiple machine learning models to classify iris species
- Saves the best model and scaler for future use

## Dataset
- **Source**: The [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris) is loaded from a CSV file.
- **Attributes**: Sepal length, Sepal width, Petal length, Petal width, and Species (target variable).

## Data Preprocessing
1. **Null Value Check**: Checks for null values; columns with >15% missing data would be dropped (none in this case).
2. **Outliers**: Visualized through box plots and scatter plots.
3. **Feature Scaling**: Standard Scaler is used to normalize the data.

## Models
The following models are trained and evaluated:
1. **Logistic Regression**
2. **K-Nearest Neighbors (KNN)**
3. **Support Vector Classifier (SVC)**
4. **Naive Bayes**

## Evaluation
Each model is evaluated using:
- **Accuracy Score**
- **Confusion Matrix**

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/hk-kumawat/irisflowerclassifier.git
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Train the model**: Run the main script to train and evaluate the models.
2. **Model Inference**:
   - Preprocess a sample input using `scaler.pkl`.
   - Use `model.pkl` to predict the iris species.

## Technologies Used
- Python
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`
- Deployment: Streamlit for UI

## Results
- Logistic Regression and SVM achieved the highest scores (100% accuracy).

## Contact

### 📬 Get in Touch!
I'd love to hear from you! Whether you have a question, suggestions, a brilliant idea, or just want to connect! Feel free to reach out:


- [![GitHub](https://img.shields.io/badge/GitHub-hk--kumawat-blue?logo=github)](https://github.com/hk-kumawat) 💻 — Dive into my projects and contributions.
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-Harshal%20Kumawat-blue?logo=linkedin)](https://www.linkedin.com/in/harshal-kumawat/) 🌐 — Grow our professional network.
- [![Email](https://img.shields.io/badge/Email-harshal.kumawat%40example.com-blue?logo=gmail)](mailto:harshal.kumawat@example.com) 📧 — Drop me an email for any detailed discussions.
