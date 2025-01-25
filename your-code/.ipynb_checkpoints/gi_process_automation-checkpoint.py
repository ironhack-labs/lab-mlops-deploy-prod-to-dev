import os
import subprocess

def run_command(command):
    """Execute a system command."""
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    if process.returncode != 0:
        print(f"Error: {process.stderr}")
    else:
        print(process.stdout)

role = input("Are you the Developer or Gatekeeper? (DEV/PRD): ").strip().upper()

if role == "DEV":
    print("---- Role: Developer ----")
    
    # Create virtual environment and set up dependencies
    print("Creating virtual environment...")
    run_command("python3 -m venv venv")
    run_command("source venv/bin/activate")

    print("Installing dependencies...")
    run_command("pip install -r requirements.txt")

    print("Generating requirements.txt...")
    run_command("pip freeze > requirements.txt")

    # Initialize Git repository
    print("Initializing Git repository...")
    run_command("git init")
    run_command("git add .")
    run_command('git commit -m "Initial commit"')

    repo_url = input("Enter the remote repository URL: ").strip()
    run_command(f"git remote add origin {repo_url}")
    run_command("git branch -M main")
    run_command("git push -u origin main")

    print("Create the Pull Request from the GitHub/GitLab interface.")

elif role == "PRD":
    print("---- Role: Gatekeeper ----")
    
    # Clone repository and set up environment
    repo_url = input("Enter the remote repository URL: ").strip()
    run_command(f"git clone {repo_url} project")
    os.chdir("project")

    print("Creating virtual environment...")
    run_command("python3 -m venv venv")
    run_command("source venv/bin/activate")

    print("Installing dependencies...")
    run_command("pip install -r requirements.txt")

    # Run the project
    print("Running the project...")
    # Replace with the actual command to run the project
    run_command("python main.py")

    print("Process completed! Provide feedback to the Developer.")

else:
    print("Invalid role. Please select DEV or PRD.")
