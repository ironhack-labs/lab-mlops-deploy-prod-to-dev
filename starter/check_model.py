"""The gatekeeper's check: run it after rebuilding the environment, before merging a pull request."""
import json
import sys

import joblib
from sklearn.metrics import roc_auc_score

from train import load_data

MIN_AUC = 0.80        # agreed by the team: no model below this reaches main


def main():
    with open("models/churn_pipeline.json") as file:
        metadata = json.load(file)
    model = joblib.load("models/churn_pipeline.joblib")
    _, X_test, _, y_test = load_data()

    problems = []
    if list(X_test.columns) != metadata["features"]:
        problems.append("the input columns differ from the ones the model was trained on")
    probabilities = model.predict_proba(X_test)[:, 1]
    if not ((probabilities >= 0) & (probabilities <= 1)).all():
        problems.append("the predictions are not probabilities")
    auc = roc_auc_score(y_test, probabilities)
    if auc < MIN_AUC:
        problems.append(f"test ROC AUC {auc:.3f} is below the agreed minimum of {MIN_AUC}")

    print(f"Model: {metadata['model']}, trained {metadata['trained_at']} with scikit-learn {metadata['scikit-learn']}")
    if problems:
        print("CHECK FAILED:\n- " + "\n- ".join(problems))
        sys.exit(1)
    print(f"CHECK PASSED: test ROC AUC {auc:.3f} (minimum {MIN_AUC})")


if __name__ == "__main__":
    main()
