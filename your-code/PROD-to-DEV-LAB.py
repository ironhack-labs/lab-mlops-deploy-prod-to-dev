import os
import subprocess

# Step 1: Create a new virtual environment
venv_path = "C:/Users/larry/python_virtual_env_project/lwd_virtual"
subprocess.run(f"python -m venv {venv_path}", shell=True)
print(f"Virtual environment created at: {venv_path}")

# Step 2: Verify that the virtual environment folder exists
if os.path.exists(venv_path):
    print(f"Contents of the virtual environment directory ({venv_path}):")
    for item in os.listdir(venv_path):
        print(f"  - {item}")
else:
    print("Error: Virtual environment was not created successfully.")

# Step 3: Show the activation command for the virtual environment (manual step)
print("\nTo activate the virtual environment, run the following command in your terminal:")
print(f"{os.path.join(venv_path, 'Scripts', 'activate')}")