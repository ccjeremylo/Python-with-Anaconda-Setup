# Python-with-Anaconda-Setup

This is a quick intro to Python with Anaconda on Windows.

---
### Dependencies

1. [Anaconda](https://www.anaconda.com/) (optional, but recommended)
2. pip (comes with anaconda)
3. python3 (comes with anaconda)
4. jupyter (comes with anaconda)
5. [git](https://git-scm.com/download/win)

---
### Setup 101

Set up a python virtual environment, aka. venv - let's name it `myenv`:

```
conda create --name myenv
```

Activate your venv

```
activate myenv
```

Install relevant python packages into your venv

```
pip install -r requirements.txt
```

Let's try to run some code! Easiest way to start is to use [Jupyter lab](https://jupyterlab.readthedocs.io/en/latest/).
Before we do that, we need to add our venv to jupyter:
```
conda install ipykernel
ipython kernel install --user --name=<any_name_for_kernel>
```
Let's launch jupyter lab now:
```
jupyter lab
```

If the above doesn't work, i.e., if you are seeing an error message like this:
```
'jupyter' is not recognized as an internal or external command
```
or this:
```
'python' is not recognized as an internal or external command
```
it might mean that the path variable for jupyter/python has not been configured properly.
Follow [this guide](https://medium.com/@viknesh2798/how-to-fix-the-issues-while-using-python-command-in-the-command-prompt-ba56d9018c5f#:~:text=This%20is%20because%2C%20the%20windows,the%20python%20from%20command%20line.) to trouble shoot.

---
### (Personal) Recommended IDEs for python!

- jupyter lab
- PyCharm
- vscode

---
### Other productivity tools to explore in the future

- [Github desktop](https://desktop.github.com/)
- [vscode](https://code.visualstudio.com/)

---
### References

- [Installing Anaconda](https://www.anaconda.com/)
- [Conda cheatsheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
- [Jupyter notebook/lab review](https://www.reviewnb.com/)
- [Git for windows](https://git-scm.com/download/win)
- [Git command cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)

