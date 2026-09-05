![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# LAB | MLOps Deployment Workflow (DEV → PROD)

## What you are shipping

In this lab, you will collaborate on a small project repository that contains **all files required to run the project** (script or notebook) and share the **exact environment** needed to run it. 

Work in pairs to simulate a real ML engineering workflow:

- **Developer** writes code and proposes it through a **Pull Request**.
- **Gatekeeper** reviews, tests, and approves changes before they reach production (`main`).
- You will **switch roles later**, so both students practice each role.

## Gatekeeper (first step)

1. Create a repo on GitHub  
2. **Add a README** → this creates the `main` branch  
3. Add your partner as a **collaborator**  
4. **Do NOT write code or run `git init`**. Your job is to **own & review**, not build.

## Developer

- Clone the repo (do **NOT** run `git init`):

  ```bash
  git clone <repo-url>
  cd <repo>
  ```

* Create a branch for your work:

  ```bash
  git checkout -b branch-name
  ```

* Add your code (all files necessary for the project)
  * **Required files (minimum)**
    * `README.md`
    * your project code (script or notebook)
    <!-- * `environment.yml` -->

* Commit and push **your branch only**:

  ```bash
  git add .
  git commit -m "Add setup files"
  git push -u origin branch-name
  ```

* Open a Pull Request → from your branch into `main`

:exclamation: If you need to update the PR, commit and push to the same branch again. The PR will update automatically.

## Gatekeeper after PR

* Review the PR and merge it
* Clone the repo:

  ```bash
  git clone <repo-url>
  cd <repo>
  ```

* Pull the latest code from `main`:

  ```bash
  git pull origin main
  ```

* Run the project code and test it (if it’s a notebook, you just open it in Jupyter/VS Code and run it)

## Gatekeeper Checklist

* Does the code run?
* Are required files present?
* Was anything unnecessary committed (env folders, caches, etc.)?

If something is wrong → request changes from Developer. Then **switch roles**.
Everyone should experience **both Developer and Gatekeeper duties**.


## BONUS: Environment Sharing (with Conda!)

Previously in this lab you learned how to collaborate safely in a team using:
- branches
- pull requests
- a Gatekeeper protecting `main`

Now we take our workflow one step closer to real MLOps:
The Developer must share the **exact environment** required to run the code,
and the Gatekeeper must **rebuild that environment** before testing it.

### What Is a Virtual Environment?

When you install libraries like pandas, numpy, or TensorFlow, they stay on your computer.

Over time your computer collects different versions of packages, and projects start **breaking each other**.
A **virtual environment** is like a **separate mini-computer inside your computer**.
It only contains the libraries (and versions) that a single project needs.


### Why environments matter in MLOps

If every machine uses the same environment, then the code will run the same everywhere:

**DEV → TEST → PROD**

This is how real ML teams ensure models don’t “work on my machine only.”

---

So, let's upgrade our lab! 💪


## Developer’s new duty

Before writing code, the Developer should now **create a Conda virtual environment for the project**.

* In **VS Code terminal** (bash):

  ```bash
  conda create -n project-env python=3.11 -y
  conda activate project-env
  ```

* Install the libraries you need (example):

  ```bash
  conda install pandas requests -y
  ```

* Work on your code normally

* Then export your environment to share it:

  ```bash
  conda env export --from-history > environment.yml
  ```

* Commit and push `environment.yml` as part of your **Pull Request**.

  * The Gatekeeper will reproduce the environment using this file.

## Gatekeeper’s new duty

After merging the PR, before testing the code:

* Recreate the environment using the Developer’s environment file:

  ```bash
  conda env create -f environment.yml -n project-env
  ```

* Activate it:

  ```bash
  conda activate project-env
  ```

* Run the project (script or notebook).

  * If it fails, the Developer must fix the environment file and update the PR.

## Things to keep in mind

* If you already created `project-env` before, you may need to remove it or use a different name.
* Consider adding a `.gitignore` so you don’t commit unnecessary files (env folders, caches, `.ipynb_checkpoints`, `__pycache__`, etc.).  
---

# Projet : analyse d'un journal de crises

Projet livre par le **Developer** pour ce lab. Il est volontairement court, mais
complet : il s'installe, il s'execute, et il produit des sorties verifiables.

## Ce que fait le code

`seizure_diary_analysis.py` genere un journal de crises **synthetique**
(aucune donnee patient reelle), en calcule quelques indicateurs — frequence
mensuelle, duree moyenne et mediane, plus long intervalle sans crise, part de
crises nocturnes, repartition par type — et ecrit trois fichiers dans `outputs/` :

| Fichier | Contenu |
|---|---|
| `journal_crises.csv` | le journal genere, une ligne par crise |
| `indicateurs.csv` | les indicateurs calcules |
| `figures.png` | repartition horaire + frequence mensuelle |

Le script est **deterministe** (graine fixee a 42) : deux executions produisent
exactement les memes chiffres. C'est ce qui permet au Gatekeeper de verifier que
l'environnement a bien ete reproduit — si les nombres different, c'est
l'environnement qui differe, pas le code.

## Installation

```bash
conda env create -f environment.yml -n project-env
conda activate project-env
```

## Execution

```bash
python seizure_diary_analysis.py
```

Option : `--crises N` pour changer le nombre de crises generees
(defaut : 120).

## Sortie attendue

Avec les parametres par defaut, l'execution doit afficher exactement :

```
120 crises generees

                             valeur
nb_crises                   120.000
duree_suivi_jours           354.000
frequence_par_30j            10.170
duree_moyenne_s              75.700
duree_mediane_s              74.500
plus_long_intervalle_jours   21.800
part_nocturnes_0h_6h          0.458
part_focale                   0.533
part_focale_bilateralisee     0.275
part_absence                  0.192
```

## Checklist Gatekeeper

- [ ] `environment.yml` est present et `conda env create -f environment.yml` aboutit
- [ ] `python seizure_diary_analysis.py` s'execute sans erreur
- [ ] les chiffres affiches correspondent exactement au bloc ci-dessus
- [ ] `outputs/` a bien ete cree, avec les trois fichiers attendus
- [ ] aucun dossier d'environnement, cache ou sortie generee n'a ete commite
      (`.gitignore` couvre `outputs/`, `__pycache__/`, `.ipynb_checkpoints/`, `.DS_Store`)
