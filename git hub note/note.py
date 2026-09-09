"""
Working Directory
       ↓
   git add
       ↓
Staging Area
       ↓
  git commit
       ↓
Local Repository
       ↓
   git push
       ↓
GitHub Remote Repository

====================================================================================================================================
                     config
                     ↓
                     init
                     ↓
                     add
                     ↓
                     commit
                     ↓
                     status
----------------------------------------------------------------------------------------------------------------------------------------
1.Adding username
→ git config --global user.name "Your Name"

2.Adding email
→ git config --global user.email "your@email.com"

3.List config details
→ git config --list

4.Initializing Git
→ git init

5.Adding all changes to staging area - untracked files
→ git add -A

6.Staged files → Local repository
→ git commit -m "commit message"

7.Working tree / untracked files
→ git status

8. add remote file
→ git remote add name path

9. Push local repository to GitHub
→ git push name master

"""