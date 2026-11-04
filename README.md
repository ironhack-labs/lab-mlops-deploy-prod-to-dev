This project trains a machine learning model to predict customer churn using Logistic Regression.

Requirements

Python 3.14.4

Create and activate a virtual environment:

python -m venv .venv
.\.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Train the model:

python train.py

Check the model:

python check_model.py

The model must achieve a ROC AUC of at least 0.80 to pass.
