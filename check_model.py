"""Gatekeeper validation: check the saved model before it is merged."""
import argparse
import json
import sys

import joblib
import numpy as np
from sklearn.metrics import roc_auc_score

from train import load_data

# Round 1 acceptance threshold. In Round 2, raise this to 0.85 as requested
# in the README (or pass --min-auc 0.85 for a non-destructive local check).
MIN_AUC = 0.80


def main(min_auc: float = MIN_AUC):
    with open("models/churn_pipeline.json", encoding="utf-8") as file:
        metadata = json.load(file)
    model = joblib.load("models/churn_pipeline.joblib")
    _, X_test, _, y_test = load_data()

    problems = []
    if list(X_test.columns) != metadata["features"]:
        problems.append("input columns differ from the model's training features")

    probabilities = model.predict_proba(X_test)[:, 1]
    if not np.isfinite(probabilities).all() or not (
        (probabilities >= 0) & (probabilities <= 1)
    ).all():
        problems.append("predictions are not finite probabilities in [0, 1]")

    auc = roc_auc_score(y_test, probabilities)
    if auc < min_auc:
        problems.append(f"test ROC AUC {auc:.3f} is below minimum {min_auc:.3f}")

    print(
        f"Model: {metadata['model']} | CV AUC: {metadata['cv_auc']:.3f} | "
        f"trained: {metadata['trained_at']} | scikit-learn: {metadata['scikit-learn']}"
    )
    if problems:
        print("CHECK FAILED:\\n- " + "\\n- ".join(problems))
        return 1
    print(f"CHECK PASSED: test ROC AUC {auc:.3f} (minimum {min_auc:.2f})")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-auc", type=float, default=MIN_AUC)
    sys.exit(main(parser.parse_args().min_auc))
