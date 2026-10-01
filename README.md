# UPI Fraud Detection System

An end-to-end machine learning project designed to identify potentially fraudulent UPI transactions using transaction-level data and classification algorithms.

## Overview

Digital payment systems such as UPI process a large number of transactions every day, making automated fraud detection an important problem.

This project uses machine learning to analyze transaction characteristics such as transaction type, amount, merchant category, location, banking information, device type, network type, and transaction timing to classify transactions as:

- **0 → Genuine Transaction**
- **1 → Fraudulent Transaction**

## Features

- Transaction amount analysis
- Transaction type analysis
- Merchant category analysis
- Sender and receiver information
- Banking information
- Device and network information
- Time-based transaction features
- Machine learning based fraud classification
- Model performance evaluation using classification metrics

## Machine Learning

The project explores multiple classification algorithms:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Naive Bayes
- Decision Tree
- Support Vector Machine (SVM)
- Random Forest

Model performance is evaluated using:

- Confusion Matrix
- Precision
- Recall
- F1-Score
- Accuracy

Since fraud detection involves highly imbalanced classes, the project focuses particularly on the model's ability to identify fraudulent transactions.

## Dataset

The project uses a UPI transaction dataset containing transaction-level information.

The dataset includes features such as:

- Transaction type
- Merchant category
- Transaction amount
- Sender age group
- Receiver age group
- Sender state
- Sender bank
- Receiver bank
- Device type
- Network type
- Hour of transaction
- Day of week
- Weekend indicator

> **Note:** The dataset used in this project is intended for educational and machine learning experimentation purposes.

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- VS Code
- Git & GitHub

## Project Structure

```text
UPI-Fraud-Detection/
│
├── notebooks/
│   └── UPI_Fraud_Detection.ipynb
│
├── .gitignore
├── README.md
└── upi_transactions_2024.csv