#!/bin/bash

# Check if running as Developer or Gatekeeper
read -p "Are you the Developer or Gatekeeper? (DEV/PRD): " ROLE

if [ "$ROLE" == "DEV" ]; then
    echo "---- Role: Developer ----"

    # Create virtual environment and prepare project
    echo "Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate

    echo "Installing dependencies..."
    pip install -r requirements.txt

    echo "Generating requirements.txt..."
    pip freeze > requirements.txt

    # Initialize Git
    echo "Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit"

    # Configure remote repository
    read -p "Enter the remote repository URL: " REPO_URL
    git remote add origin $REPO_URL
    git branch -M main
    git push -u origin main

    echo "Create the Pull Request from the GitHub/GitLab interface."
elif [ "$ROLE" == "PRD" ]; then
    echo "---- Role: Gatekeeper ----"

    # Pull changes from the repository
    read -p "Enter the remote repository URL: " REPO_URL
    git clone $REPO_URL project
    cd project

    # Create virtual environment and verify dependencies
    echo "Creating virtual environment and setting up the environment..."
    python3 -m venv venv
    source venv/bin/activate

    echo "Installing dependencies..."
    pip install -r requirements.txt

    # Run the project
    echo "Running the project..."
    # Replace the following command with the actual project execution command
    python main.py

    echo "Process completed! Provide feedback to the Developer."
else
    echo "Invalid role. Please select DEV or PRD."
fi
