# Iris-Flower-Classifier🌸

![51518iris img1](https://github.com/user-attachments/assets/c6f757d5-250e-4237-9e19-ebbd40a2c2b3)

## Overview

This project classifies iris flower species (Setosa, Versicolor, Virginica) using various classification models, including Logistic Regression, K-Nearest Neighbors (KNN), Support Vector Machine (SVM), and Naive Bayes. The models are trained on the Iris dataset and evaluated to determine the best-performing model.

## Live Demo

Take a look at my Iris flower classifier [![Experience It! 🌟](https://img.shields.io/badge/Experience%20It!-blue)](https://iris-species-predictor.streamlit.app)

<br>

- _Below is a preview_of the Iris Flower Classifier in action. The app allows users to input the sepal and petal dimensions to predict the species of the Iris flower. Check out the sleek interface and accurate predictions!_ 👇🏻🪻

![Screenshot 2024-10-30 134720](https://github.com/user-attachments/assets/57e2fef9-a067-4e98-8b24-7d6df5342b50)


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
10. [Conclusion](#conclusion)
11. [Contact](#contact)

<br>

## Features🌟

- Loads and cleans the Iris dataset
- Scales input features for consistent model performance
- Trains multiple machine learning models to classify iris species
- Saves the best model and scaler for future use

<br>

## Dataset📊

- **Source**: The [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris) is loaded from a CSV file.
- **Attributes**: Sepal length, Sepal width, Petal length, Petal width, and Species (target variable).

<br>

## Data Preprocessing🛠

1. **Null Value Check**: Checks for null values; columns with >15% missing data would be dropped (none in this case).
2. **Outliers**: Visualized through box plots and scatter plots.
3. **Feature Scaling**: Standard Scaler is used to normalize the data.

<br>

## Models🧠

The following models are trained and evaluated:
1. **Logistic Regression**
2. **K-Nearest Neighbors (KNN)**
3. **Support Vector Classifier (SVC)**
4. **Naive Bayes**

<br>

## Evaluation📈

Each model is evaluated using:
- **Accuracy Score**
- **Confusion Matrix**

<br>

## Installation🛠

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hk-kumawat/irisflowerclassifier.git

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

<br>

## Usage🚀
1. **Train the model**: Run the main script to train and evaluate the models.
2. **Model Inference**:
   - Preprocess a sample input using `scaler.pkl`.
   - Use `model.pkl` to predict the iris species.

<br>

## Technologies Used💻
- Python
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`
- Deployment: Streamlit for UI


<br>

## Results🏆
- Logistic Regression and SVM achieved the highest scores (100% accuracy).

<br>  

## Conclusion📚
- The Iris Flower Classification project successfully demonstrates the power of machine learning models in solving a classic classification problem. By training and evaluating multiple models (Logistic Regression, K-Nearest Neighbors, Support Vector Machine, and Naive Bayes), we identified Logistic Regression and SVM as the most accurate classifiers for this dataset. With the pre-trained model and scaler saved for future use, this application provides a streamlined approach for predicting iris species based on sepal and petal measurements.

- This project highlights the importance of data preprocessing, feature scaling, and model selection in building robust machine learning applications. Furthermore, deploying the model on Streamlit allows for an accessible, user-friendly experience, showcasing the practical application of machine learning in real-time.

<br>

## Contact

### 📬 Get in Touch!
I'd love to hear from you! Whether you have a question, suggestions, a brilliant idea, or just want to connect! Feel free to reach out:


- [![GitHub](https://img.shields.io/badge/GitHub-hk--kumawat-blue?logo=github)](https://github.com/hk-kumawat) 💻 — Dive into my projects and contributions.
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-Harshal%20Kumawat-blue?logo=linkedin)](https://www.linkedin.com/in/harshal-kumawat/) 🌐 — Grow our professional network.
- [![Email](https://img.shields.io/badge/Email-harshal.kumawat%40example.com-blue?logo=gmail)](mailto:harshal.kumawat@example.com) 📧 — Drop me an email for any detailed discussions.
