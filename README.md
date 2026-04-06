# lab-mlops-deploy-prod-to-dev

A lab project demonstrating an MLOps workflow for deploying from a production environment to a development environment.

## Project Structure

```
├── main.py              # Entry point
├── pyproject.toml       # Project metadata and dependencies
├── requirements.txt     # Pinned dependencies
├── uv.lock              # Lockfile for reproducible installs
└── .gitignore
```

## Prerequisites

- Python 3.8+
- [`uv`](https://github.com/astral-sh/uv) (recommended) **or** `pip`

## Setup

### Clone the repository

```bash
git clone https://github.com/richim96/lab-mlops-deploy-prod-to-dev.git
cd lab-mlops-deploy-prod-to-dev
```

### Create and activate a virtual environment

**Using `uv` (recommended):**

```bash
uv venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows
```

**Using standard `venv`:**

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows
```

### Install dependencies

**Using `uv`:**

```bash
uv pip install -r requirements.txt
```

**Using `pip`:**

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Git Workflow

This project follows a `prod → dev` deployment pattern using Git branches:

- `main` — production branch
- `dev` — development branch

To sync changes from `main` into `dev`:

```bash
git checkout dev
git merge main
git push origin dev
```

To contribute:

```bash
git checkout -b feat/your-feature
# make your changes
git add .
git commit -m "feat: describe your change"
git push origin feat/your-feature
```

Then open a pull request into `dev`.