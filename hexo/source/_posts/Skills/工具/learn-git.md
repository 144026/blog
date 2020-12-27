---
title: learn-git
date: 2020-11-20 16:17:15
categories:
- 技能
tags:
- git
---

git notes.

<!--more-->

# 1 commands

## 1.1 start

`git init`

`git clone $url [$dir]`

similar to:

```bash
mkdir $dir && cd $dir
git init
git remote add origin $url
git fetch origin
git switch -c master origin/master # create local branch from remote tracking branch
# git branch -u origin/master master # set upstream
```

## 1.2 current change

`git add`
- `add -u`
- `add .`
- `add -A`

`git commit`

`git rm|mv`

## 1.3 state and history

`git status|log|show`

- `git log --graph --prettey=formate:'' --abbrev-commit`

`git diff|grep`

## 1.4 grow, mark and tweak

`git switch`

- `git switch <branch>`
- `git switch -c <newbranch> [<start_point>]`


`git branch`

- `git branch -vva`
- `git branch <newbranch> [<start_point>]`
- `git branch [-cCmMdD <branch>]`
- `git branch -u <remote_ref> <branch>` (`git config --global push.default upstream`)

`git merge|rebase`

- `git merge <branch>`: merge `<branch>` into current branch

`git reset|restore`

`git tag`

## 1.5 collaborate

`git remote`

- `git remote add|remove|rename|prune|set-url`

`git fetch`

- `git fetch [<remote>] [<remote_branch>]`

`git pull`

- `git fetch origin && git merge $upstream`?

`git push`

- `git push [<remote>] [+][src]:[dst]`
- `git push -u <remote> <localbranch>`


# 2

# 3
