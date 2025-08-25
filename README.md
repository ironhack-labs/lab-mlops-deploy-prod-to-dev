# Environment Setup (macOS with Conda)

## 1. Create Environment
```bash
conda create -n myenv python=3.11
conda activate myenv
2. Install Dependencies
# From requirements.txt
conda install --file requirements.txt

# OR from environment.yml (preferred)
conda env create -f environment.yml
3. Export Environment
# Export to text file
conda list --export > requirements.txt

# Export full environment with channels
conda env export > environment.yml
4. Use in VS Code
Open project in VS Code
Press Cmd + Shift + P → Python: Select Interpreter
Choose your conda environment (myenv)
5. Deactivate
conda deactivate
