# Issues and Resolutions Report — MLOps Deployment Workflow (DEV → PROD)

This report documents the technical issues encountered while completing the lab and how
each was resolved, following the Developer → Gatekeeper workflow with a shared, reproducible
Conda environment (`environment.yml`).

## Context

- **Goal:** collaborate on a small project repo (notebook + environment) using branches,
  Pull Requests, and a Gatekeeper protecting `main`.
- **Reproducibility:** the runtime environment is shared via `environment.yml` so any
  collaborator can recreate it with `conda env create -f environment.yml`.

## Issue 1 — Cross-platform dependency broke environment creation (macOS → Windows)

- **Symptom:** `conda env create -f environment.yml` failed for a collaborator on Windows.
- **Cause:** the environment included `python.app`, a **macOS-only** package (it has no
  Windows build), so Conda could not resolve the environment off macOS.
- **Resolution:** removed `python.app` from `environment.yml` so the environment is
  cross-platform. After the fix, `conda env create -f environment.yml` succeeds on both
  macOS and Windows.
- **Trace:** commits `fix: remove macOS-specific python.app dependency for Windows compatibility`
  and `Remove python.app from environment.yml`.
- **Lesson:** pin only dependencies that are portable across the team's operating systems;
  OS-specific packages must not live in a shared environment file.

## Issue 2 — Dependency management for reproducibility

- **Symptom:** dependencies were initially tracked ad hoc, which is fragile for sharing.
- **Resolution:** consolidated dependencies into `environment.yml` (Conda) as the single
  source of truth for the runtime, so the Gatekeeper can recreate the exact environment
  before testing the Developer's code.
- **Lesson:** an explicit environment file is part of the deliverable, not an afterthought —
  it is what makes "runs on my machine" become "runs on the team's machines".

## Issue 3 — Keeping the Pull Request in sync

- **Symptom:** uncertainty about how to update a PR after pushing more work.
- **Resolution:** confirmed that pushing additional commits to the **same branch**
  automatically updates the open PR (no need to reopen or recreate it).
- **Lesson:** a PR tracks a branch, not a fixed commit; iterate on the branch and the
  review thread stays in one place.

## Outcome

The shared environment now installs cleanly across operating systems, the project code
(notebook) runs from that environment, and changes flow through a branch → Pull Request →
`main` process reviewed by the Gatekeeper.
