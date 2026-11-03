# churn-mlops
MLOps deployment workflow lab
# Churn Prediction — MLOps Workflow

## Project Overview

This project implements a machine learning pipeline for predicting customer churn using Logistic Regression.

The purpose of the project is to demonstrate a reproducible MLOps workflow, including model training, validation, dependency management, and GitHub pull request reviews.

## Requirements

- Python 3.x (replace with the version used)
- pandas
- scikit-learn
- joblib

## Setup

Clone the repository and navigate to the project folder.

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Train the Model

```powershell
python train.py
```

This trains a Logistic Regression model and saves the resulting pipeline to `models/churn_pipeline.joblib`.

## Validate the Model

```powershell
python check_model.py
```

The validation script verifies that the test ROC AUC meets the minimum threshold of 0.8.

## Reproducibility

The trained model is deliberately excluded from Git through `.gitignore`.

Reviewers can recreate it from the committed code, dataset, and dependency specifications.

## Git Workflow

Development takes place on feature branches. Changes are submitted through pull requests and reviewed before being merged into `main`.