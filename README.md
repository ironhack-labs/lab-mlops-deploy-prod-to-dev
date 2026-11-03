![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# LAB | MLOps Deployment Workflow (DEV → PROD)

## What you are shipping

In this lab you work **in pairs** on one shared repository, the way an ML team does. The project is the churn model from the **MLOps Essentials** lesson: `starter/train.py` trains a pipeline and saves it with its metadata, and `starter/check_model.py` is the check that must pass before anything reaches `main`.

- The **Developer** writes code on a branch and proposes it through a **pull request (PR)**.
- The **Gatekeeper** owns `main`: they rebuild the environment **from the repository alone**, run the check, and merge only if everything passes.
- In round 2 you **switch roles**, and the new Developer ships a better model.

**By the end, you can:**

1. Apply the DEV → PROD workflow: a branch, a pull request, a review and a merge into `main`.
2. Make a project reproducible with a virtual environment and a pinned `requirements.txt`, and verify that a partner can rebuild it.

**Time:** about 2 hours for both rounds. **Prerequisites:** git and GitHub from the first weeks, and today's lesson (virtual environments, `requirements.txt`, saving a pipeline, the DEV → PROD workflow).

## Round 1: ship the first model

### Gatekeeper: create the repository (5 minutes)

1. On GitHub, create a new **public** repository (for example `churn-mlops`) and tick **Add a README**: this creates the `main` branch.
2. Add your partner as a **collaborator** (Settings → Collaborators).
3. Do **not** write code. Your job is to own and review `main`.

### Developer: prepare the project on a branch

1. Clone the repository (do **not** run `git init`) and create a branch:

   ```bash
   git clone <repo-url>
   cd <repo>
   git checkout -b first-model
   ```

2. Copy the contents of this lab's `starter` folder into the repository: `train.py`, `check_model.py` and `data/churn.csv`.
3. Create a virtual environment **inside the project**, install only what the project needs, and run it:

   ```bash
   python -m venv .venv
   source .venv/bin/activate            # Windows: .venv\Scripts\activate
   pip install pandas scikit-learn joblib
   python train.py
   python check_model.py
   ```

   **First checkpoint:** `train.py` prints `Saved models/churn_pipeline.joblib: LogisticRegression, cv_auc 0.816, test_auc 0.818`, and `check_model.py` prints `CHECK PASSED: test ROC AUC 0.818 (minimum 0.8)`.

4. Write a `requirements.txt` with your **direct** dependencies, pinned to the versions you have (find them with `pip freeze` or `pip show pandas`), for example:

   ```
   pandas==2.3.3
   scikit-learn==1.6.1
   joblib==1.5.3
   ```

5. Add a `.gitignore` with at least `.venv/`, `models/`, `__pycache__/` and `.ipynb_checkpoints/`. The model is **not** committed: the Gatekeeper rebuilds it from the code and the data, which proves the project is reproducible.
6. Update the `README.md`: what the project does, the Python version you used, and the commands to run it.
7. Commit and push **your branch only**, then open a pull request from `first-model` into `main`:

   ```bash
   git add train.py check_model.py data/churn.csv requirements.txt .gitignore README.md
   git commit -m "First churn model, with requirements and model check"
   git push -u origin first-model
   ```

   **Second checkpoint:** the pull request shows six files and no `.venv` or `models` folder.

### Gatekeeper: review, rebuild, check, merge

1. Read the pull request on GitHub. Use the checklist below, and leave at least one comment.
2. Fetch the branch and rebuild the environment **from scratch**, in a new virtual environment:

   ```bash
   git clone <repo-url> && cd <repo>          # or: git fetch && git checkout first-model
   git checkout first-model
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   python train.py
   python check_model.py
   ```

3. If anything fails, **request changes** in the pull request and explain what went wrong. The Developer fixes it on the same branch; the pull request updates by itself.
4. When the check passes, **merge** the pull request into `main`.

   **Third checkpoint:** `main` contains the project, the check passed on the Gatekeeper's machine, and the pull request has at least one review comment.

### Gatekeeper checklist

- Does the environment rebuild from `requirements.txt` alone?
- Do `train.py` and `check_model.py` run, and does the check pass?
- Are the required files present: code, data, `requirements.txt`, `.gitignore`, README?
- Was anything committed that should not be: `.venv`, `models`, caches, `.env` files or keys?
- Does the README say how to run the project?

## Round 2: switch roles and ship a better model

The former Gatekeeper is now the Developer, and the other way round.

1. **New Developer:** pull `main`, create a branch `better-model`, rebuild the environment, and improve the model in `train.py`. For example, replace the logistic regression with a random forest (`RandomForestClassifier(n_estimators=200, random_state=42)`) or gradient boosting, as in the lesson. Update `requirements.txt` if you add a library. Run `train.py` and `check_model.py`, then open a pull request whose description gives the **old and the new** `cv_auc`.
2. **New Gatekeeper:** review, rebuild, run the check and merge only if it passes **and** the new model is better than the one on `main` by cross-validation. Before you merge, ask the Developer in a review comment to raise `MIN_AUC` in `check_model.py` to `0.85` in the same pull request: the team's bar goes up with every better model.

   **Fourth checkpoint:** two merged pull requests in the repository's history, one per round, each reviewed by the other person. With a random forest, `train.py` prints a `cv_auc` of about 0.92 and a `test_auc` of about 0.89.

## Bonus

Choose one:

- **Conda instead of venv.** Repeat round 1 with `conda create -n churn python=3.12`, `conda env export --from-history > environment.yml` and `conda env create -f environment.yml`. What does `environment.yml` contain that `requirements.txt` does not?
- **Automatic checks (continuous integration).** Add a GitHub Actions workflow that runs the check on every pull request, so the Gatekeeper sees the result before even opening the code. Save this as `.github/workflows/check.yml`:

  ```yaml
  name: Model check
  on: pull_request
  jobs:
    check:
      runs-on: ubuntu-latest
      steps:
        - uses: actions/checkout@v4
        - uses: actions/setup-python@v5
          with:
            python-version: "3.12"
        - run: pip install -r requirements.txt
        - run: python train.py
        - run: python check_model.py
  ```

  Open a pull request with a deliberately worse model (for example `LogisticRegression(C=0.0001)`) and watch the check fail on GitHub.

## Deliverables

- The URL of your shared repository, with **two merged pull requests** (one per round), each reviewed by the other person. Both partners submit the same URL.

## Submission

Submit the URL of the shared repository in the platform. Both partners must be able to see their own review comments and merges in the repository's history.

## Data

`starter/data/churn.csv` is the telecom churn dataset used in Weeks 4 and 5 of the course.
