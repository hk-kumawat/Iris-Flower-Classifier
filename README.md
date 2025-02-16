<a id="readme-top"></a>

# Iris-Flower-Classifier🌸

![51518iris img1](https://github.com/user-attachments/assets/c6f757d5-250e-4237-9e19-ebbd40a2c2b3)

## Overview

This project is an Iris Flower Classifier built using **Streamlit** and **scikit-learn**. It leverages a machine learning model trained on the classic **Iris** dataset to predict the species of an iris flower based on four features: sepal length, sepal width, petal length, and petal width. The project includes an interactive web app where users can input flower measurements and receive real-time predictions.



<br>


## Live Demo

Take a look at my Iris flower classifier! 👉🏻 [![Experience It! 🌟](https://img.shields.io/badge/Experience%20It!-blue)](https://iris-species-predictor.streamlit.app)

<br>

 _Below is a preview_of the Iris Flower Classifier in action. The app allows users to input the sepal and petal dimensions to predict the species of the Iris flower. Check out the sleek interface and accurate predictions!_ 👇🏻🪻


![Screenshot 2024-10-31 033404](https://github.com/user-attachments/assets/230ffc01-7457-4a8c-937f-0a7ee4c7801c)

<br>

## Learning Journey 🗺️

This project represents my journey into classical machine learning problems and interactive web applications. Here's the story behind it:

- **Inspiration:**  
  The Iris dataset is a cornerstone of machine learning education. I wanted to transform this academic staple into a practical, user-friendly tool while learning core ML concepts.

- **Why I Made It:**  
  I aimed to create a system that not only classifies Iris flowers accurately but also serves as an educational tool for understanding ML concepts like data preprocessing, model selection, and deployment.

- **Challenges Faced:**  
  - **Model Selection:** Evaluating different ML algorithms to find the best performer.
  - **Data Preprocessing:** Implementing proper scaling and encoding techniques.
  - **UI/UX Design:** Creating an intuitive interface for users to input measurements.
  - **Model Deployment:** Packaging the ML model with a web interface effectively.

- **What I Learned:**  
  - **Machine Learning Pipeline:** End-to-end ML project implementation
  - **Data Analysis:** Advanced visualization and statistical analysis
  - **Model Comparison:** Evaluating multiple ML algorithms
  - **Web Development:** Building interactive ML applications with Streamlit

<br>


## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Technologies Used](#technologies-used)
5. [Dataset](#dataset)
6. [Data Preprocessing](#data-preprocessing)
7. [Model Training](#model-training)
8. [Model Performance](#model-performance)
9. [Directory Structure](#directory-structure)
10. [Contributing](#contributing)
11. [License](#license)
12. [Contact](#contact)

<br>

## Features🌟

- **Accurate Classification:**  
  Uses a machine learning model to predict iris species with high accuracy.
- **Interactive Input:**  
  Users can enter sepal and petal measurements via an intuitive Streamlit interface.
- **Real-Time Predictions:**  
  Instant feedback on the predicted species.
- **Data Visualization:**  
  The model training notebook includes visualizations for data exploration and model performance.
- **Model Persistence:**  
  Trained 'model' and 'scaler' are saved as pickle files for efficient re-use.

<br>


## Installation🛠

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/hk-kumawat/Iris-Flower-Classifier.git
   cd Iris-Flower-Classifier
   ```

2. **Create & Activate a Virtual Environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate       # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Use Dev Container:**
   - Open the project in your IDE using the configuration in `.devcontainer/devcontainer.json` for a containerized setup.

<br>


## Usage🚀

1. **Launch the Streamlit app:**
```bash
streamlit run app.py
```

2. **Enter flower measurements:**
   - Sepal Length (cm)
   - Sepal Width (cm)
   - Petal Length (cm)
   - Petal Width (cm)

3. **Click "Classify My Flower" to get predictions**

### Jupyter Notebook
Explore the model development process:
```bash
jupyter notebook "Iris_Flower_Classification.ipynb"
```

<br>

## Technologies Used💻

- **Programming Language:**  
  - Python

- **Machine Learning:**  
  - scikit-learn  
  - Logistic Regression, KNN, SVM, Naive Bayes

- **Data Handling & Visualization:**  
  - Pandas  
  - NumPy  
  - Matplotlib  
  - Seaborn

- **Web Framework:**  
  - Streamlit

- **Model Persistence:**  
  - pickle

<br>


## Dataset📊

This project uses the classic **Iris** dataset, which contains:
- **Features:**  
  - Sepal Length, Sepal Width, Petal Length, Petal Width
- **Output:**  
  - Iris Species (Setosa, Versicolor, Virginica)
- **Data Source:**  
 The [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris) is loaded from a CSV file.

<br>


## Data Preprocessing🔄

- **Data Cleaning:**  
  Initial analysis of the dataset to check for null values and duplicates.
- **Feature Selection:**  
  Selecting sepal and petal dimensions as inputs.
- **Label Encoding:**  
  Converting the categorical species names into numerical labels.
- **Scaling:**  
  Using StandardScaler to normalize feature values for consistent model performance.


<br>

## Model Training🧠

- **Training Process:**  
  The notebook trains multiple models (Logistic Regression, KNN, SVM, Naive Bayes) to compare performance.
- **Model Evaluation:**  
  Evaluates models using accuracy scores and confusion matrices.
- **Model Persistence:**  
  The best performing model and the scaler are saved as `model.pkl` and `scaler.pkl`, respectively.

<br>


## Model Performance🏆

### Accuracy Scores:
- **Logistic Regression:** 100%
- **SVM:** 100%
- **KNN:** 96%
- **Naive Bayes:** 96%

### System Metrics:
- **Average Prediction Time:** <1s
- **Model Size:** 4KB
- **Scalability:** Can handle multiple concurrent users
- **Validation Accuracy:** 98%

<br>  

## Directory Structure📁

```plaintext
hk-kumawat-iris-flower-classifier/
├── README.md                        # Project documentation
├── Iris.csv                         # Dataset file
├── Iris_Flower_Classification.ipynb  # Model development notebook
├── app.py                           # Streamlit application
├── model.pkl                        # Trained model
├── scaler.pkl                       # Fitted scaler
├── requirements.txt                 # Dependencies
└── .devcontainer/                   # Development container config
    └── devcontainer.json
```

<br>

## Contributing🤝
Contributions make the open source community such an amazing place to learn, inspire, and create. 🙌 Any contributions you make are greatly appreciated! 😊

Have an idea to improve this project? Go ahead and fork the repo to create a pull request, or open an issue with the tag **"enhancement"**. Don't forget to give the project a star! ⭐ Thanks again! 🙏

<br>

1. **Fork** the repository.

2. **Create** a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Commit** your changes with a descriptive message.

4. **Push** to your branch:
   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open** a Pull Request detailing your enhancements or bug fixes.

<br> 


## License📝

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

<br>


## Contact

### 📬 Get in Touch!
I'd love to hear from you! Whether you have a question, suggestions, a brilliant idea, or just want to connect! Feel free to reach out:


- [![GitHub](https://img.shields.io/badge/GitHub-hk--kumawat-blue?logo=github)](https://github.com/hk-kumawat) 💻 — Dive into my projects and contributions.
- [![LinkedIn](https://img.shields.io/badge/LinkedIn-Harshal%20Kumawat-blue?logo=linkedin)](https://www.linkedin.com/in/harshal-kumawat/) 🌐 — Grow our professional network.
- [![Email](https://img.shields.io/badge/Email-harshalkumawat100@.com-blue?logo=gmail)](mailto:harshalkumawat100@gmail.com) 📧 — Drop me an email for any detailed discussions.

<br>


## Thanks for exploring—happy classifying! 🌸

> "Where flowers bloom, so does hope." – Lady Bird Johnson

<p align="right">(<a href="#readme-top">back to top</a>)</p>
