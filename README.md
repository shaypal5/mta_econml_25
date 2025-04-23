# 📊 Intro to Machine Learning for Economics & Management

Welcome to the course repository for **Intro to Machine Learning for Economics and Management**! This course is designed for B.Sc. students with little to no technical background in machine learning. Through a hands-on, problem-solving approach using real-world datasets, you’ll learn to think like a data scientist and gain the foundational skills needed to understand, manage, and contribute to ML-driven projects in business, finance, and policy.

---

## 🧭 Course Structure

This repository is organized into two main parts, each structured around a practical, industry-inspired use case.

### 📁 `part_1_churn`
**Theme:** Customer Churn Prediction  
**Industry Context:** Telecom  
**Goal:** Learn how to model binary classification problems (predicting whether a customer will churn) using decision trees and ensemble methods.  
**Key Topics:**
- Regression vs classification
- Handling imbalanced datasets
- Model selection and evaluation
- Pipelines and basic serialization

📍 Includes:
- Raw and preprocessed churn datasets
- Notebook exercises and solutions
- Utility scripts and helper functions


---

## Slides

### Part 1.B: Imbalanced Learning:

https://docs.google.com/presentation/d/1jGhnVrhwJV8TiTEyvurNGV0ZFx9wbPfvmXbIW0o9ahY/edit?usp=sharing

## 💻 Repo Layout Overview

```
intro_to_ml_repo/
├── README.md                   ← This file
├── dir_struct.sh              ← Shell script for reproducing repo structure
├── part_1_churn/              ← Churn prediction project
│   ├── churn_train.csv        ← Training data
│   ├── churn_test.csv         ← Test data
│   ├── hex1/                  ← Hex session with exercises and solutions
│   └── session_4/             ← Exercises for advanced data imbalance topics
├── part_2_fraud/              ← Fraud detection project
│   ├── data/                  ← Raw and prepared datasets
│   ├── notebooks/             ← EDA, modeling, and analysis notebooks
│   └── problem_generation/    ← Tools for creating new fraud challenges
```

---

## 📂 Data Sources

- **Churn Dataset**: Provided by CrowdAnalytix for a churn prediction competition. It contains 3,333 customer records with 20 usage-related features. About 14% of customers in the dataset are churners.
  - [Dataset on Kaggle](https://www.kaggle.com/datasets/mnassrib/telecom-churn-datasets/data)
  - [Competition page](https://www.crowdanalytix.com/contests/why-customer-churn)
  - [Reference paper (IRJET)](https://www.irjet.net/archives/V3/i4/IRJET-V3I4213.pdf)

- **Fraud Dataset**: Synthesized financial transactions with realistic fraud labels for exploring anomaly detection and rare event prediction.

---

## 🧠 Learning Objectives

By the end of this course, you’ll be able to:
- Frame business and economic problems as machine learning tasks
- Choose appropriate models and evaluation metrics
- Preprocess data and engineer meaningful features
- Manage modeling workflows and interpret ML outputs
- Collaborate effectively with data science professionals

---

## 📌 Notes for Students

- Most notebooks contain both **exercise** (`_ex.ipynb`) and **solution** (`_sol.ipynb`) versions.
- Use the `README.md` files within each project part for more context on specific exercises.
- Code is written in Python, using libraries such as `pandas`, `scikit-learn`, and `xgboost`.

---

📬 Questions or feedback? Please reach out via the course communication platform or in-class discussions.

Happy learning!  
— *The Course Team*
