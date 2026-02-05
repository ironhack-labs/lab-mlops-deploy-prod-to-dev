# MLOps Lab Report: Deployment from DEV to PROD

**Student:** Julia Parnis  
**Date:** February 5, 2026  
**Repository:** https://github.com/JuliaP-create/streamlit-iris-analysis  
**Exercise:** MLOps Deployment Workflow Simulation

---

## Summary

Successfully completed end-to-end MLOps deployment workflow including:
- Feature development on isolated branch
- Pull request creation
- Fresh environment testing
- Code review and approval
- Merge to production

---

## Part 1: Developer Role

### Initial Setup

**Files Created:**
1. `.gitignore` - Excluded venv and temporary files
2. `README.md` - Comprehensive documentation
3. `requirements.txt` - Dependency management

**Git Repository:**
- Initialized git repository
- Created GitHub repository: streamlit-iris-analysis
- Pushed initial code to main branch

### Feature Development

**Feature:** CSV Download Button

**Branch Strategy:**
- Created feature branch: `feature/add-download-button`
- Isolated development from main branch

**Code Changes:**
```python
# Added to iris_analysis.py
st.markdown("---")
st.subheader("📥 Download Dataset")
csv = iris_df.to_csv(index=False)
st.download_button(
    label="Download Iris Dataset as CSV",
    data=csv,
    file_name="iris_dataset.csv",
    mime="text/csv"
)
```

### Testing:
- Tested locally before committing
- Verified download button functionality
- Confirmed no breaking changes

### Git workflow
```bash
git checkout -b feature/add-download-button
# Made changes
git add iris_analysis.py
git commit -m "Add CSV download button feature"
git push origin feature/add-download-button
```
**Pull Request:**
- Created PR on GitHub
- Added description of changes
- Included testing instructions

## Part 2: Gatekeeper Role

### Code Review Process

**Actions Taken:**
1. Reviewed Pull Request on GitHub
2. Examined code changes
3. Verified requirements.txt was updated (if needed)
4. Checked README documentation

### Testing in Fresh Environment

**Test Setup:**
- Location: C:\Julia\Ironhack\iris-gatekeeper-test\
- Fresh clone from GitHub
- New virtual environment
- Clean installation from requirements.txt

**Commands executed:**
```bash
git clone https://github.com/JuliaP-create/streamlit-iris-analysis.git
cd streamlit-iris-analysis
git checkout feature/add-download-button
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run iris_analysis.py
```
### Test Results:
✅ Application launched successfully
✅ Download button displayed correctly
✅ Download functionality worked
✅ No errors in console
✅ All dependencies installed without issues

### Approval & Merge
- Provided positive feedback on Pull Request
- Approved merge to main branch
- Merged feature branch
- Delete feature branch (cleanup) - to be done after submission

## Challenges Faced & Solutions

### Challenge 1: Missing requirements.txt Initially

**Problem:**
First deployment to Streamlit Cloud failed with ModuleNotFoundError

**Cause:**
Did not create requirements.txt before initial deployment

**Solution:**
- Created requirements.txt with necessary packages.
- Committed and pushed to GitHub
- Re-deployed successfully

### Challenge 2: Confusion with Git Branches

**Problem:**
Initially unclear how changes on feature branch were separated from main

**Cause:**
New to Git branching workflow

**Solution:**
- Learned that Git changes file content based on active branch
- Same physical file has different content per branch
- Used git checkout to switch and verify

### Challenge 3: Terminal venv Confusion

**Problem:**
When switching from Git Bash to CMD terminal, saw (venv) prompt but in different folder

**Cause:**
CMD inherited activated venv from original project

**Solution:**
- Ran deactivate to clear old venv
- Created fresh venv in gatekeeper test folder
- Activated new venv

