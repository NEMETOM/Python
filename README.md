
======================================
# Working Directory
- Area where all our files and directories and changes are living all the time 

# Staging Area
- Files and directories that we explicitly add to the staging area
- Add Files:
git add <file name>

- Check status
git status


# Git Repository
- Where all our snapshots are stored
- Commit files:
git commit -m "add message"

# ==============================
# Move file from c9 to GitHub
# ==============================

# Add remote node
git remote add origin git@github.com:NEMETOM/Python.git

# Move Files
git push -u origin master

# See status
git remote -v

