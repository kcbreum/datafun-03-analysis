# datafun-03-analytics

Professional analytics project using Git, Python, venv, pip, and VS Code to raed and process data.
Commands were used on a Windows machine running PowerShell.

## Create Project Virtual Environment

On Windows, create a project virtual environment in the .venv folder. 

```shell

py -m venv .venv
.venv\Scripts\Activate
py -m pip install -r requirements.txt

```
## Freeze Requirements

```shell
py -m pip freeze > requirements.txt
```

## Git add and commit 

```shell
git add .
git commit -m "add .gitignore, cmds to readme"
git push origin main
```

## Specification

This project was built to the following specification:

- [datafun-03-spec](https://github.com/denisecase/datafun-03-spec)