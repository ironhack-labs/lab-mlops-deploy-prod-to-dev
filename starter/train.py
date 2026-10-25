"""Train the churn model and save it, with its metadata, in the models folder."""
import json
import os
import sys
from datetime import datetime, timezone
from importlib.metadata import version

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

CATEGORICAL = ["Int'l Plan", "VMail Plan"]


def load_data(path="data/churn.csv"):
    churn = pd.read_csv(path)
    y = (churn["Churn?"] == "True.").astype(int)
    X = churn.drop(columns=["Churn?", "Phone", "Area Code", "State"])
    return train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)


def make_pipeline():
    numeric = ["Account Length", "VMail Message", "Day Mins", "Day Calls", "Day Charge", "Eve Mins", "Eve Calls",
               "Eve Charge", "Night Mins", "Night Calls", "Night Charge", "Intl Mins", "Intl Calls", "Intl Charge",
               "CustServ Calls"]
    preprocessing = ColumnTransformer([("categorical", OneHotEncoder(drop="if_binary"), CATEGORICAL),
                                       ("numeric", StandardScaler(), numeric)])
    return Pipeline([("preprocessing", preprocessing), ("model", LogisticRegression(max_iter=1000))])


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_data()
    pipeline = make_pipeline()
    cv_auc = cross_val_score(pipeline, X_train, y_train, cv=5, scoring="roc_auc").mean()
    pipeline.fit(X_train, y_train)
    test_auc = roc_auc_score(y_test, pipeline.predict_proba(X_test)[:, 1])

    os.makedirs("models", exist_ok=True)
    joblib.dump(pipeline, "models/churn_pipeline.joblib")
    metadata = {
        "model": type(pipeline.named_steps["model"]).__name__,
        "trained_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "features": list(X_train.columns),
        "cv_auc": round(cv_auc, 3),
        "test_auc": round(test_auc, 3),
        "python": sys.version.split()[0],
        "scikit-learn": version("scikit-learn"),
    }
    with open("models/churn_pipeline.json", "w") as file:
        json.dump(metadata, file, indent=2)
    print(f"Saved models/churn_pipeline.joblib: {metadata['model']}, cv_auc {cv_auc:.3f}, test_auc {test_auc:.3f}")
