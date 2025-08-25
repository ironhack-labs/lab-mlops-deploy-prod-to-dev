### Report

During the exercise, our group encountered an issue when trying to activate the virtual environment in Windows PowerShell.
The activation script (`Activate.ps1`) was blocked due to PowerShell’s default execution policy (`Restricted`).
We resolved this by temporarily bypassing the restriction for the current session using `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`,
after which the environment activated successfully. As alternatives, we noted that activation also works via Command Prompt (`activate.bat`) or Git Bash (`source activate`). The main lesson learned was that PowerShell’s security policies can interfere with Python workflows, and the safest approach is to use a temporary bypass to continue development without permanent system changes.
