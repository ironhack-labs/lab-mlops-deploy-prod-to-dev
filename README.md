# NYC Taxi Trip Duration Prediction — MLflow Experiment Tracking

Predict taxi trip duration using NYC Green Taxi data with MLflow for experiment tracking, model management, and model registry.

## Project Structure

```
.
├── 01_Linear_Model_example.ipynb     # Baseline linear regression
├── 02_Xgboost_example.ipynb          # XGBoost with hyperparameter tuning (Hyperopt)
├── 03_Ensemble_example.ipynb         # Ensemble model combining multiple approaches
├── running-mlflow-examples/          # MLflow collaboration scenarios (1-3)
├── environment.yml                   # Conda environment specification
├── requirements.txt                  # Pip dependencies
└── .gitignore
```

## Setup

### 1. Create and activate the Conda environment

```bash
conda env create -f environment.yml -n project-env
conda activate project-env
```

### 2. Launch MLflow UI

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Then open `https://127.0.0.1:5000` in your browser.

### 3. Run the notebooks

Open any notebook in Jupyter or VS Code and run all cells:

```bash
jupyter notebook
```

## Notebooks Overview

| Notebook | Description |
|---|---|
| `01_Linear_Model_example.ipynb` | Baseline model using linear regression with MLflow tracking |
| `02_Xgboost_example.ipynb` | XGBoost model with Hyperopt tuning, model logging, and registry |
| `03_Ensemble_example.ipynb` | Ensemble combining multiple models for improved performance |
| `scenario-1.ipynb` | Single data scientist workflow |
| `scenario-2.ipynb` | Cross-functional team with one data scientist |
| `scenario-3.ipynb` | Multiple data scientists collaborating |

## Data

NYC Green Taxi trip records (January–March 2021) in Parquet format, stored in the `Data/` directory.

## Dependencies

- Python 3.11
- MLflow
- scikit-learn
- XGBoost
- Hyperopt
- pandas, seaborn
- Jupyter
