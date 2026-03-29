## STEPS TO DO IN TERMINAL
1.  Create a new environment
python -m venv venv

2.  Git ignore venv folder
echo "venv" > .gitignore

3. Activate Environment
Linux: . ./venv/bin/activate

4.  Install dependencies (if you forked the repo jump to 6)
python -m pip install pandas

5.  Freeze dependencies
python -m pip freeze > requirements.txt

6.  Install dependencies from requirements.txt
python -m pip install -r requirements.txt

7.  Run the project
python -m test