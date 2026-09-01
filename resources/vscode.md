# Visual Studio Code (VS Code)

Related pages: [Resources Home](./README.md) | [Unit 1 Resources](./unit-1-research-computing.md) | [Syllabus](../syllabus.md)

Visual Studio Code, usually called VS Code, is a free, open-source editor for writing code, editing text files, using the command line, and working with Git in one place. In this course, it will be a practical home base for opening project folders, editing Python files, running shell commands, and managing version control.

## Why We Use It In This Course

- Open an entire project folder and keep files, scripts, and notes together.
- Use the integrated terminal to run commands such as `pwd`, `ls`, `python`, and `git status`.
- Work with Git through either the terminal or the built-in Source Control panel.
- Stay in one application instead of switching constantly between an editor, a terminal, and a Git client.

## Download And Install On macOS

1. Download VS Code from the [official download page](https://code.visualstudio.com/Download) or the [macOS setup guide](https://code.visualstudio.com/docs/setup/mac).
2. Open the downloaded `.dmg` file.
3. Drag `Visual Studio Code.app` into the `Applications` folder.
4. Open VS Code from `Applications`.
5. To make the `code` command available in Terminal, open the Command Palette with `Shift` + `Command` + `P`, search for `Shell Command: Install 'code' command in PATH`, and run it.
6. Open a course folder with `File > Open Folder...`, or open a folder from Terminal by running `code .` inside that folder.

## Download And Install On Windows

1. Download VS Code from the [official download page](https://code.visualstudio.com/Download) or the [Windows setup guide](https://code.visualstudio.com/docs/setup/windows).
2. For most students, choose the Windows User Installer, which is the recommended setup from the VS Code documentation.
3. Run the installer and follow the prompts.
4. After installation, open PowerShell or Command Prompt in a project folder and try `code .` to launch that folder in VS Code.
5. You can also open a folder from inside VS Code with `File > Open Folder...`.

## Using VS Code For Course Work

1. Open your course repository or project folder.
2. Open the integrated terminal with `View > Terminal`.
3. Run course commands directly in that terminal, such as `git status`, `python --version`, or course scripts.
4. Edit files in the main editor area and save your changes normally.
5. Use the Source Control view to review changes, stage files, and make commits if you prefer a graphical Git workflow.

## Python Virtual Environments

For course assignments, use a separate Python virtual environment inside each project repository. This keeps the packages for one project from interfering with the packages for another project.

On macOS or Git Bash, open the VS Code terminal in your project folder and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install numpy scipy matplotlib pandas ipykernel ipython
```

The general pattern is:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install package1 package2 package3
```

Replace `package1 package2 package3` with the needed packages for the assignment. For most course notebooks, the needed packages will include `numpy`, `scipy`, `matplotlib`, `pandas`, and `ipykernel`. Installing `ipython` is also helpful because it gives you the `ipython` command in the VS Code terminal.

After installing packages, you can record the environment with:

```bash
pip freeze > requirements.txt
```

Commit `requirements.txt` to Git, but do not commit the `.venv/` directory. Add `.venv/` to `.gitignore` for each project.

On Windows PowerShell, the equivalent commands are:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install numpy scipy matplotlib pandas ipykernel ipython
```

After creating the environment, open a `.ipynb` notebook in VS Code and click `Select Kernel`. Choose the Python interpreter from the `.venv` folder in your project.

## Git In VS Code

VS Code has built-in Git support, but it uses the Git installation already on your computer.

- Check whether Git is available by running `git --version` in the VS Code terminal.
- If Git is not installed yet, use the [official Git download page](https://git-scm.com/downloads) and then restart VS Code.
- Once Git is installed, VS Code can detect repositories automatically when you open a folder that already contains a Git repository.

## Suggested First Steps

- Open the course repository in VS Code.
- Open the terminal and run `pwd` to confirm where you are.
- Check that Python is available with `python3 --version` on macOS or `py --version` on Windows.
- Run `git status` to see the current repository state.
- Create and activate a project `.venv`.
- Open a notebook and select the `.venv` kernel.
- Create or edit a small file so you can practice saving changes and checking the Source Control panel.

## Troubleshooting Python And Notebooks

- Install the Microsoft Python and Jupyter extensions in VS Code.
- Open the whole project folder in VS Code, not just an individual file.
- If `python3` is not found on macOS, install Python from [python.org](https://www.python.org/downloads/) and reopen the terminal.
- If `py` is not found on Windows, install Python from [python.org](https://www.python.org/downloads/) and make sure the Python launcher is included.
- If package imports fail, activate `.venv` and run `pip install package-name` again.
- If the notebook still cannot import an installed package, use `Select Kernel` and choose the `.venv` interpreter.
- If PowerShell blocks `.venv\Scripts\Activate.ps1`, you can use Git Bash, Command Prompt, or install packages with `.venv\Scripts\python -m pip install package-name`.
- To check which Python your terminal is using, run `which python` on macOS or Git Bash, or `where python` on Windows.
- To check which packages are installed in the active environment, run `pip list`.
- To check the interactive Python shell, run `python` and then type `exit()`.
- To check IPython, run `ipython` after installing it in the active environment.

## Official References

- [VS Code overview](https://code.visualstudio.com/docs/getstarted/overview)
- [Python in VS Code](https://code.visualstudio.com/docs/languages/python)
- [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments)
- [Jupyter notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)
- [Jupyter kernel management in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-kernel-management)
- [Integrated terminal](https://code.visualstudio.com/docs/terminal/getting-started)
- [Source control in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview)
