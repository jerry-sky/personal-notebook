# Git notes

- [Removing a commit](#removing-a-commit)
- [Removing a file from git history](#removing-a-file-from-git-history)
- [Fix displaying file names with unicode characters in them](#fix-displaying-file-names-with-unicode-characters-in-them)

## Removing a commit

First, remove the commit from local repository using a command like `git reset --soft [commit]^`.
Then, if necessary force-push to remote repository e.g. GitHub to remove that commit from there as well.

[Further reading](https://stackoverflow.com/a/448929)

## Removing a file from git history

Follow the tutorial [here](https://help.github.com/en/github/authenticating-to-github/removing-sensitive-data-from-a-repository).

## Fix displaying file names with unicode characters in them

For some odd reason `git` doesn't properly display non-ASCII characters (exotic characters e.g. ö or ę) in file and directory names. To fix it execute:
```bash
git config --global core.quotePath false
```
