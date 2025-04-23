
# LangChain + OpenAI + MultiQueryRetriever Project

## ✅ Overview
This project demonstrates a full implementation of a question-answering pipeline using LangChain, OpenAI, and MultiQueryRetriever. It includes secure API usage, modular setup, reproducibility with requirements.txt, and Git version control simulation.

---

## 1. 🧑‍💻 Developer Role: Project Setup, Version Control & Pull Request

- Developed inside a Jupyter Notebook `main2.ipynb` using Python.
- Installed necessary packages: `langchain`, `faiss-cpu`, `python-dotenv`, `openai`, and others.
- Saved environment dependencies via:
  ```bash
  pip freeze > requirements.txt
  ```
- Initialized a Git repository and performed standard Git operations:
  ```bash
  git init
  git add .
  git commit -m "initial commit"
  git remote add origin <repo_url>
  git push -u origin main
  ```
- Opened a Pull Request for peer review.

---

## 2. ✅ Gatekeeper Role: Review, Pull, Setup, and Run Project

- Simulated a gatekeeper review:
  - Cloned the repository.
  - Created a new virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # or .\venv\Scripts\activate on Windows
    pip install -r requirements.txt
    jupyter notebook main2.ipynb
    ```
  - Ran all notebook cells to verify the project setup.
- Outcome: ✅ Successfully ran with no errors.

---

## 3. ✅ Report: Process & Issue Resolution

### Problem Encountered:
- API key was accidentally exposed in a previous version.
- GitGuardian flagged the secret in a public commit.

### Resolution:
- Deleted exposed key and revoked it from OpenAI dashboard.
- Created a new key and placed it in `.env` file.
- Ensured `.env` is added to `.gitignore` to prevent future leaks.

### Reflection:
- Learned importance of secret management and reproducibility.
- Practiced MLOps workflow including development, peer review, and clean environment validation.

---

## 🔁 How to Reproduce

```bash
git clone <repo_url>
cd <project_folder>
python3 -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook main2.ipynb
```

Make sure you have a `.env` file with:
```
OPENAI_API_KEY=your_key_here
```

---

## 📝 Files Included
- `main2.ipynb`: Main implementation notebook.
- `requirements.txt`: Project dependencies.
- `temp.json`: Sample data file.
- `.env`: (not included for security) should contain your OpenAI API key.

---

Project is fully functional, documented, and secured.
