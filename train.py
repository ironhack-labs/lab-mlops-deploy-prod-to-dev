"""Train a reproducible telecom churn-classification pipeline.

Run from the project root:
    python train.py                       # Round 1: Logistic Regression
    python train.py --model random_forest # Round 2: improved Random Forest
"""
from __future__ import annotations

import argparse
import json
import os
import platform
from datetime import datetime, timezone
from importlib.metadata import version

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

CATEGORICAL = ["Int'l Plan", "VMail Plan"]
NUMERIC = [
    "Account Length", "VMail Message", "Day Mins", "Day Calls", "Day Charge",
    "Eve Mins", "Eve Calls", "Eve Charge", "Night Mins", "Night Calls",
    "Night Charge", "Intl Mins", "Intl Calls", "Intl Charge", "CustServ Calls",
]
TARGET = "Churn?"
DROP_COLUMNS = [TARGET, "Phone", "Area Code", "State"]


def load_data(path: str = "data/churn.csv"):
    """Load data, encode the binary target, and make a stratified holdout split."""
    churn = pd.read_csv(path)
    y = (churn[TARGET] == "True.").astype("int8")
    X = churn.drop(columns=DROP_COLUMNS)
    return train_test_split(
        X, y, test_size=0.20, stratify=y, random_state=42
    )


def make_pipeline(model_name: str = "logistic"):
    """Build preprocessing + estimator as one leakage-safe sklearn Pipeline."""
    preprocessing = ColumnTransformer(
        transformers=[
            ("categorical", OneHotEncoder(drop="if_binary", handle_unknown="ignore"), CATEGORICAL),
            ("numeric", StandardScaler(), NUMERIC),
        ],
        remainder="drop",
    )

    if model_name == "logistic":
        estimator = LogisticRegression(max_iter=1000, random_state=42)
    elif model_name == "random_forest":
        # A fixed seed makes the comparison reproducible.
        estimator = RandomForestClassifier(
            n_estimators=200, random_state=42, n_jobs=-1,
            class_weight=None,
        )
    else:
        raise ValueError("model_name must be 'logistic' or 'random_forest'")

    return Pipeline([("preprocessing", preprocessing), ("model", estimator)])


def train(model_name: str = "logistic", data_path: str = "data/churn.csv"):
    """Cross-validate on training data, fit once, and persist model + metadata."""
    X_train, X_test, y_train, y_test = load_data(data_path)
    pipeline = make_pipeline(model_name)

    # CV is performed only on the training partition. The holdout test set
    # remains untouched until the final evaluation.
    cv_scores = cross_val_score(
        pipeline, X_train, y_train, cv=5, scoring="roc_auc", n_jobs=-1
    )
    pipeline.fit(X_train, y_train)
    test_probabilities = pipeline.predict_proba(X_test)[:, 1]
    test_auc = roc_auc_score(y_test, test_probabilities)

    os.makedirs("models", exist_ok=True)
    model_path = "models/churn_pipeline.joblib"
    metadata_path = "models/churn_pipeline.json"
    joblib.dump(pipeline, model_path)

    metadata = {
        "model": type(pipeline.named_steps["model"]).__name__,
        "model_name": model_name,
        "trained_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "features": list(X_train.columns),
        "cv_auc": float(cv_scores.mean()),
        "cv_auc_std": float(cv_scores.std(ddof=1)),
        "test_auc": float(test_auc),
        "python": platform.python_version(),
        "scikit-learn": version("scikit-learn"),
        "pandas": version("pandas"),
        "joblib": version("joblib"),
        "random_state": 42,
    }
    with open(metadata_path, "w", encoding="utf-8") as file:
        json.dump(metadata, file, indent=2)

    print(
        f"Saved {model_path}: {metadata['model']}, "
        f"cv_auc {cv_scores.mean():.3f}, test_auc {test_auc:.3f}"
    )
    return pipeline, metadata, (X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--model", choices=["logistic", "random_forest"], default="logistic",
        help="Estimator to train (default: logistic, Round 1).",
    )
    parser.add_argument("--data", default="data/churn.csv", help="CSV path.")
    args = parser.parse_args()
    train(args.model, args.data)
