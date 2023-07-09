# 🧑‍🏭 Setup

> [Pyenv](https://www.wolfremium.dev/blog/python-multiple-versions) >
> [Makefile](https://hernandis.me/2017/03/20/como-hacer-un-makefile.html)

After `pyenv` installation, run this in this directory:

```bash
pyenv install 3.10.9
```

Set default Python version for current directory:

```bash
pyenv local 3.10.9
```

Basic setup to use pipenv.

```bash
python -m pip install -U pip && pip install pipenv
```

This project includes make commands to make your life easier.

```bash
sudo apt-get install make
```

Install all the dependencies, and generates a virtual environment.

```bash
make setup
```

## 💩 Troubleshooting

- [Select VSCode Interpreter (modules not found after installation)](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)
