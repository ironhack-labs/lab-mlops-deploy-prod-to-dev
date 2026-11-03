# Telecom Churn — MLOps Deployment Workflow (DEV → PROD)

This project reproduces the supplied Ironhack lab and adds an executable notebook. It trains a binary churn classifier, saves the complete preprocessing/model pipeline and metadata, and validates the saved artifact before promotion.

## Project structure

```text
.
├── data/churn.csv
├── models/                 # generated locally; intentionally git-ignored
├── notebooks/
│   └── MLOps_Deployment_Workflow.ipynb
├── train.py
├── check_model.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Environment and run

Use Python 3.11–3.13 (the dependency pins are the versions used to validate this package).

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

# Round 1: baseline Logistic Regression
python train.py
python check_model.py

# Round 2: improved Random Forest
python train.py --model random_forest
python check_model.py --min-auc 0.85
```

The notebook can be opened from the project root with `jupyter notebook` or `jupyter lab`. It walks through the data, model design, evaluation, artifact checks, and deployment workflow.

## What the pipeline does

1. Reads `data/churn.csv`.
2. Converts `Churn?` (`True.` / `False.`) into a binary target.
3. Excludes `Phone`, `Area Code`, and `State` from predictors. The identifier-like phone number is not a meaningful generalizable predictor; the supplied starter also excludes state and area code.
4. Uses a stratified 80/20 train/test split (`random_state=42`).
5. One-hot encodes the two binary plan columns and standardizes numerical predictors inside a `ColumnTransformer`.
6. Evaluates with five-fold ROC-AUC cross-validation on the training partition, then fits the pipeline and evaluates once on the held-out test partition.
7. Saves the fitted pipeline to `models/churn_pipeline.joblib` and metrics/environment metadata to `models/churn_pipeline.json`.
8. `check_model.py` reloads those artifacts and checks feature consistency, valid probabilities, and the agreed minimum test ROC-AUC.

Keeping preprocessing inside the sklearn `Pipeline` is important: each CV fold learns its own scaling/encoding parameters from that fold's training data, avoiding preprocessing leakage.

## Expected results

With the fixed split and random seeds, results should be close to:

| Round | Model | Mean 5-fold CV ROC-AUC | Holdout test ROC-AUC |
|---|---|---:|---:|
| 1 | Logistic Regression | 0.816 | 0.818 |
| 2 | Random Forest (200 trees) | 0.920 | 0.889 |

Small differences can occur across library versions and platforms. ROC-AUC measures ranking quality across thresholds; it is not accuracy and does not establish that predicted probabilities are calibrated.

## DEV → PROD collaboration workflow

The notebook documents the commands, but GitHub collaboration still requires two people and a remote repository.

### Round 1

- Gatekeeper creates a GitHub repository with `main`, adds the Developer as collaborator, and does not write the model code.
- Developer clones it, creates `first-model`, adds the project files, runs both commands above, commits and pushes only that branch, then opens a PR into `main`.
- Gatekeeper reviews the PR, leaves at least one review comment, clones/fetches the branch into a fresh environment, installs from `requirements.txt`, reruns training and the check, then merges only if the check passes.
- Verify that `.venv/`, `models/`, caches, secrets, and local notebook checkpoints are not committed.

### Round 2

- Switch roles. The new Developer branches from updated `main` as `better-model`, trains `python train.py --model random_forest`, and opens a PR describing both CV-AUC values.
- The new Gatekeeper reviews the change and requires the acceptance threshold to rise from `0.80` to `0.85` (the CLI equivalent is `python check_model.py --min-auc 0.85`). Rebuild in a clean environment, rerun the check, and merge only if the Random Forest improves CV-AUC and passes the raised acceptance bar.
- The expected Random Forest CV-AUC is about 0.92 and holdout ROC-AUC about 0.89.

**Important:** a local run cannot create the two real GitHub pull requests, reviews, collaborator actions, or merges. Those are deliberate human/team deliverables and must be completed in GitHub.

## Bonus: continuous integration

A GitHub Actions workflow can run on each pull request. The README in the original brief provides a starter YAML. For a robust workflow, use `actions/setup-python`, install `requirements.txt`, run training, and run `check_model.py`. Keep the workflow in `.github/workflows/check.yml`.

## Limitations and responsible interpretation

- This is a teaching exercise using a historical, imbalanced telecom dataset (about 14.5% churn). It is not a production-ready retention system.
- The random train/test split is reproducible but does not test performance under temporal or customer-population drift.
- ROC-AUC alone is insufficient for business decisions. A real deployment would also assess calibration, precision/recall at an operational threshold, costs of false positives/negatives, fairness across relevant groups, monitoring, and retraining.
- The provided features include highly related usage-minute and charge variables; this is acceptable for a predictive baseline but should be considered when interpreting feature importance.
