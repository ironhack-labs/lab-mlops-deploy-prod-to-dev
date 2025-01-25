# LAB | MLOps Deployment from PROD to DEV

## Activity Explanation

The activity consists of simulating a realistic process of deploying code from a development environment (DEV) to a production environment (PRD), working in pairs to represent the roles of a developer (Developer) and a production manager (Gatekeeper). This process is common in professional software development environments and follows best practices for version control, code review and environment configuration.

## Main Objective
Prepare participants for real-world work scenarios such as continuous deployments (CI/CD), teamwork, and handling tools like Git and Python.

## Process Automation
To facilitate this process, scripts (in Unix Shell Script and Python) automate much of the repetitive work, ensuring that the flow can be completed in a faster and more structured manner.

### How the code works:
The script detects the user's role (Developer or Gatekeeper) at startup.

### Depending on the role:
- Developer:
    - Sets up a virtual environment.
    - Generates a requirements.txt file.
    - Initializes a Git repository and connects it to a remote repository.
    - Indicates that the Pull Request must be created manually from the remote repository's web interface.
- Gatekeeper:
    - Clones the remote repository.
    - Creates a virtual environment in production.
    - Installs the necessary dependencies.
    - Runs the project to verify its functionality.

### Expected Outcome
- A complete and successful flow of code deployment between development and production.
- Each participant should have:
    - Committed code from a development environment to a remote repository.
    - Reviewed, merged, and executed code in a production environment.
A brief report documenting:
    - The steps taken.
    - Issues encountered and how they were resolved.
    - Lessons learned.