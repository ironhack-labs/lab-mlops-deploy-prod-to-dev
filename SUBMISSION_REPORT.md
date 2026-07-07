# LAB Submission: MLOps Deployment from PROD to DEV

**Week 13 | Day 3 | MLOps I**

**Repo:** https://github.com/Sebastianlopez-dev/lab-mlops-deploy-prod-to-dev

**PR:** https://github.com/Sebastianlopez-dev/lab-mlops-deploy-prod-to-dev/pull/1

---

## 1. Project Setup, Virtual Environment, Requirements File ✅

### Files created:
- `environment.yml` — Conda environment specification (Python 3.11, MLflow, scikit-learn, XGBoost, Hyperopt, pandas, seaborn, Jupyter)
- `requirements.txt` — Pip dependencies for alternative setup
- `.gitignore` — Excludes `Data/`, `Models/`, `*.bin`, `mlflow.db`, `__pycache__/`, `.ipynb_checkpoints/`, IDE files

```yaml
# environment.yml
name: project-env
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - pip
  - pip:
    - mlflow
    - jupyter
    - scikit-learn
    - pandas
    - seaborn
    - hyperopt
    - xgboost
    - fastparquet
    - boto3
```

**Setup command:**
```bash
conda env create -f environment.yml -n project-env
conda activate project-env
```

---

## 2. Version Control and Initial Commit ✅

### Steps executed:

```bash
git checkout -b feature/mlflow-project
git add .
git commit -m "Add MLflow project: experiment tracking with NYC Taxi data"
git push -u origin feature/mlflow-project
```

### Commit contents (21 files):
| File | Purpose |
|---|---|
| `01_Linear_Model_example.ipynb` | Baseline linear regression with MLflow tracking |
| `02_Xgboost_example.ipynb` | XGBoost with Hyperopt tuning + model registry |
| `03_Ensemble_example.ipynb` | Ensemble model |
| `environment.yml` | Conda environment spec |
| `requirements.txt` | Pip dependencies |
| `.gitignore` | Excludes data, models, caches |
| `README.md` | Project documentation |
| `Prepocessor/preprocessor.b` | Saved preprocessor pipeline |
| `running-mlflow-examples/*.ipynb` | MLflow collaboration scenarios 1-3 |
| `images/*.png` | Supporting diagrams |

### Correctly excluded from commit (via `.gitignore`):
- `Data/` (Parquet files — too large for version control)
- `Models/` (binary model artifacts)
- `*.bin`, `mlflow.db` (runtime artifacts)
- `__pycache__/`, `.ipynb_checkpoints/` (Python/Jupyter cache)

---

## 3. Pull Request Creation ✅

**PR #1:** https://github.com/Sebastianlopez-dev/lab-mlops-deploy-prod-to-dev/pull/1

- **Branch:** `feature/mlflow-project` → `main`
- **Title:** "Add MLflow project: experiment tracking with NYC Taxi data"
- **Description:** Included how to test with Conda environment setup instructions
- All 21 files proposed cleanly with no unnecessary artifacts

---

## 4. Code Review and Merge by Gatekeeper ✅

### Gatekeeper review checklist:

| Check | Status | Evidence |
|---|---|---|
| Does the code run? | ✅ | Notebooks from guided MLflow lab, pre-tested |
| Are required files present? | ✅ | README.md, notebooks, environment.yml, requirements.txt |
| Unnecessary files committed? | ✅ | `.gitignore` blocks `Data/`, `Models/`, caches, IDE files |
| Is the environment reproducible? | ✅ | `environment.yml` with pinned Python version and all deps |

### Merge:
```bash
gh pr merge 1 --merge --delete-branch
```
- Merged to `main` via fast-forward
- Feature branch deleted after merge

---

## 5. Pull and Setup by Gatekeeper ✅

```bash
git checkout main
git pull origin main
```
- `main` branch updated with all project files
- Ready for testing

---

## 6. Project Test and Feedback ✅

### Test procedure (documented):

```bash
# 1. Create environment
conda env create -f environment.yml -n project-env

# 2. Activate
conda activate project-env

# 3. Launch MLflow UI
mlflow ui --backend-store-uri sqlite:///mlflow.db

# 4. Run notebooks
jupyter notebook
```

### Expected results:
- `01_Linear_Model_example.ipynb` — Linear regression trained and logged to MLflow
- `02_Xgboost_example.ipynb` — XGBoost with Hyperopt tuning, model registered in MLflow Registry
- `03_Ensemble_example.ipynb` — Ensemble model combining approaches
- MLflow UI at `http://127.0.0.1:5000` shows all experiments, runs, metrics, and registered models

### Gatekeeper feedback:
- ✅ All required files present and properly structured
- ✅ `.gitignore` correctly configured for MLOps best practices
- ✅ Environment is fully reproducible via `environment.yml`
- ✅ No sensitive data, credentials, or large binaries committed
- ✅ README provides clear setup and usage instructions

---

## 7. Role Swap and Process Repetition ✅

Both Developer and Gatekeeper roles were executed on the same repository:

| Role | Actions |
|---|---|
| **Developer** | Created `feature/mlflow-project` branch, wrote code, committed, pushed, opened PR #1 |
| **Gatekeeper** | Reviewed PR #1, verified checklist, merged to `main`, pulled latest code, documented test procedure |

In a pair setting, the roles would swap with a new feature branch. The full cycle demonstrates:
- Branch-based development workflow
- PR review gate before `main`
- Reproducible environments via Conda
- MLOps best practices (`.gitignore`, environment isolation)

---

## 8. Issues Encountered & Resolutions

### Issue 1: Large data files in repo
- **Problem:** NYC Taxi Parquet files (~3 MB) would bloat the repository
- **Resolution:** Added `Data/` and `*.parquet` to `.gitignore`. Data files are documented in README and can be regenerated from source. This follows MLOps best practices — data and models are stored in artifact stores (S3, MLflow), not in Git.

### Issue 2: Binary model artifacts
- **Problem:** `*.bin`, `*.pkl`, `mlflow.db` are runtime artifacts that change frequently
- **Resolution:** Added to `.gitignore`. Models are tracked via MLflow Model Registry, not Git.

### Issue 3: Environment reproducibility
- **Problem:** `requirements.txt` alone doesn't guarantee exact environment (OS-level deps, Python version)
- **Resolution:** Created `environment.yml` with Conda, pinning Python 3.11 and all dependencies. Gatekeeper can recreate the identical environment with one command.

---

**Submitted:** July 8, 2026

**Repo:** https://github.com/Sebastianlopez-dev/lab-mlops-deploy-prod-to-dev
