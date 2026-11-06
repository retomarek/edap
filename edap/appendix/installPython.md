# Python Installation & IDE Setup

This page covers local Python installation and IDE setup. If you just want to try the notebooks without installing anything, use [Google Colab](https://colab.research.google.com/) as described in the [Getting Started](../gettingStarted) chapter.

## Python Installation

Download and install the latest Python version from the official website:

- [python.org/downloads](https://www.python.org/downloads/)

### Windows

1. Download the installer from [python.org](https://www.python.org/downloads/)
2. **Important:** Check "Add Python to PATH" during installation
3. Open a terminal and verify: `python --version`

### macOS

1. Download the installer from [python.org](https://www.python.org/downloads/) or use Homebrew:
   ```bash
   brew install python
   ```
2. Verify: `python3 --version`

### Linux

Python is usually pre-installed. To install or update:
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

## Choose an IDE

An IDE (Integrated Development Environment) helps you write, run, and debug code more efficiently.

### Visual Studio Code
**Best for:** General-purpose development, web projects, or if you work with multiple languages
- Free, lightweight, and highly extensible via plugins
- Download: [code.visualstudio.com](https://code.visualstudio.com/)
- Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for syntax highlighting, IntelliSense, and Jupyter support
- Built-in terminal and Git integration

### PyCharm
**Best for:** Larger Python projects, software engineering, and teams
- Download (free and paid tiers): [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
- Powerful refactoring tools, built-in debugger, and project-wide code navigation

```{tip}
**Not sure which to pick?** Choose **VS Code** if you want flexibility and plan to do more than just Python, **PyCharm** if you're building larger applications or working in a team. VS Code runs Jupyter Notebooks directly in the editor.
```

## Using Jupyter Notebooks Locally

### In VS Code

1. Open a `.ipynb` file or create a new one via `Ctrl+Shift+P` → "Create: New Jupyter Notebook"
2. Select a Python kernel (interpreter) from the top-right dropdown
3. Run cells with `Shift+Enter`

### In JupyterLab

1. Install JupyterLab: `pip install jupyterlab`
2. Start it: `jupyter lab`
3. Create a new notebook from the launcher
