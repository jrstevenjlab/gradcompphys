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

## Git In VS Code

VS Code has built-in Git support, but it uses the Git installation already on your computer.

- Check whether Git is available by running `git --version` in the VS Code terminal.
- If Git is not installed yet, use the [official Git download page](https://git-scm.com/downloads) and then restart VS Code.
- Once Git is installed, VS Code can detect repositories automatically when you open a folder that already contains a Git repository.

## Suggested First Steps

- Open the course repository in VS Code.
- Open the terminal and run `pwd` to confirm where you are.
- Run `git status` to see the current repository state.
- Create or edit a small file so you can practice saving changes and checking the Source Control panel.

## Official References

- [VS Code overview](https://code.visualstudio.com/docs/getstarted/overview)
- [Integrated terminal](https://code.visualstudio.com/docs/terminal/getting-started)
- [Source control in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview)
