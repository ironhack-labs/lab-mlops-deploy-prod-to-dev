### MLOPS

### Create a venv with pip

How to create a requirements.txt file using pip
Create a new environment : `$python -m venv 'env_name'`
Activate new environment:

- Windows: `$'env_name'\Scripts\activate`;
- Mac: `source env_name/bin/activate`
  See that there are no packages in it: `$pip freeze`
  Instal a Package: `$pip install numpy`
  Check the package: `$pip freeze`
  Save the packages list: `$pip freeze > requirements.txt`
  Deactivate environment: `$deactivate`

---

When you ever need to install many packages in another envirionemnt: `$pip install -r requirements.txt`
