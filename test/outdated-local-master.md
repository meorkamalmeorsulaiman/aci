# Updated machine
```
kamal@Meors-MacBook-Pro aci % git branch 
  main
* main-a
  main-b
kamal@Meors-MacBook-Pro aci % git log --oneline
413f1a3 (HEAD -> main-a, origin/main-a, origin/main, origin/HEAD, main) Create 03-get-tenant.py
4141480 Create 03-get-tenant.py
9a42c55 Create fabric-lists.txt
df3335d (origin/adding-fab-dict) Create fabric-lists.txt
6cd4d25 Create 01-test-login.py
c133ebe Create 01-test-login.py
e620993 Adding dir for REST api
5b350eb Initial commit
```


# Outdated machine

Current branch `main-a` with commit `c813934` 
```
ansible@JUMP01:~/aci$ git branch
  main
* main-a
  main-b
ansible@JUMP01:~/aci$ git log --oneline
c813934 (HEAD -> main-a, origin/main-b, origin/main-a, main-b) adding main-a
413f1a3 (origin/main, origin/HEAD, main) Create 03-get-tenant.py
4141480 Create 03-get-tenant.py
9a42c55 Create fabric-lists.txt
df3335d (origin/adding-fab-dict) Create fabric-lists.txt
6cd4d25 Create 01-test-login.py
c133ebe Create 01-test-login.py
e620993 Adding dir for REST api
5b350eb Initial commit
```

Try to get the update
```
ansible@JUMP01:~/aci$ git pull origin main-a
From github.com:meorkamalmeorsulaiman/aci
 * branch            main-a     -> FETCH_HEAD
 + c813934...413f1a3 main-a     -> origin/main-a  (forced update)
Already up to date.
ansible@JUMP01:~/aci$ git log --oneline
c813934 (HEAD -> main-a, origin/main-b, main-b) adding main-a
413f1a3 (origin/main-a, origin/main, origin/HEAD, main) Create 03-get-tenant.py
4141480 Create 03-get-tenant.py
9a42c55 Create fabric-lists.txt
df3335d (origin/adding-fab-dict) Create fabric-lists.txt
6cd4d25 Create 01-test-login.py
c133ebe Create 01-test-login.py
e620993 Adding dir for REST api
5b350eb Initial commit
```

Quick fix is just to remove the outdated branch `main-a`
```
ansible@JUMP01:~/aci$ git branch
  main
* main-a
  main-b
ansible@JUMP01:~/aci$ git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
ansible@JUMP01:~/aci$ git branch -D main-a
Deleted branch main-a (was c813934).
```

Then create again with the updated commit
```
ansible@JUMP01:~/aci$ git checkout main-a
branch 'main-a' set up to track 'origin/main-a'.
Switched to a new branch 'main-a'
ansible@JUMP01:~/aci$ git pull origin main-a
From github.com:meorkamalmeorsulaiman/aci
 * branch            main-a     -> FETCH_HEAD
Already up to date.
ansible@JUMP01:~/aci$ git log --oneline
413f1a3 (HEAD -> main-a, origin/main-a, origin/main, origin/HEAD, main) Create 03-get-tenant.py
4141480 Create 03-get-tenant.py
9a42c55 Create fabric-lists.txt
df3335d (origin/adding-fab-dict) Create fabric-lists.txt
6cd4d25 Create 01-test-login.py
c133ebe Create 01-test-login.py
e620993 Adding dir for REST api
5b350eb Initial commit
```
