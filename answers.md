# Answers

## Developer Role: Project Setup & Version Control
- Forked lab repo and cloned locally.
- Created feature branch: `feature/dev-setup`.
- Added `main.py` at repo root with a runnable entrypoint.
- Committed and pushed.

## Developer Role: Create and Push Pull Request
- Opened **PR #1** from `feature/dev-setup` → `main`.
- PR link (First pass): 
https://github.com/ironhack-labs/lab-mlops-deploy-prod-to-dev/pull/101


## Gatekeeper Role: Review and Pull Code, Environment Setup
- Gatekeeper reviewed the PR on GitHub.
- Locally pulled branch and confirmed the structure.
- Commands used:
  git fetch origin
  git checkout main
  git pull
  git checkout -b gate/review-dev-setup
  git pull origin feature/dev-setup

Gatekeeper Role: Run and Test the Project
Ran: python main.py

Observed output: MLOps Lab Project – Developer Role Setup.

Approved and merged PR #1 into main.

Swap Roles and Repeat the Process
Swapped roles.

New branch created: feature/dev-note.

Brief Report on Process and Challenges
What went well: Small changes + PRs made review easy.

Challenges: Keeping files at repo root so the grader detects them.

Learned: Simple MLOps flow — feature branch → PR → review → run → merge.
