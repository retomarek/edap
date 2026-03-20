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

### Spyder
**Best for:** Data analysis, scientific computing, and beginners coming from MATLAB
- Free and open-source: [spyder-ide.org](https://www.spyder-ide.org/)
- Ships ready-to-use with Anaconda — minimal setup required
- Variable explorer lets you inspect data like in Excel; integrated IPython console and plot viewer

### PyCharm
**Best for:** Larger Python projects, software engineering, and teams
- Community Edition (free): [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
- Powerful refactoring tools, built-in debugger, and project-wide code navigation
- Professional Edition adds database tools and web development (Django, FastAPI) features

```{tip}
**Not sure which to pick?**

- Start with **Spyder** (via Anaconda) if your focus is data analysis and you do not have already VS Code.
- Choose **VS Code** if you want flexibility and plan to do more than just Python.
- Go with **PyCharm** if you're building larger applications or working in a team.

Both VS Code and PyCharm support Jupyter Notebooks directly in the IDE — no separate Jupyter server needed. Spyder alone does not, but installed via Anaconda it includes as well a Jupyter server.
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

### In PyCharm (via Anaconda)

PyCharm Professional has built-in Jupyter Notebook support. With Anaconda as interpreter:

1. Open Anaconda Navigator and launch **PyCharm** (or open PyCharm directly)
2. Go to `File` → `Settings` → `Project Interpreter` and select your Anaconda environment
3. Open a `.ipynb` file — PyCharm renders it as an interactive notebook
4. Run cells with `Shift+Enter`, output appears directly below each cell

```{tip}
Jupyter Notebook support is only available in **PyCharm Professional**, not in the free Community Edition. As a student or teacher, you can get a free Professional license via [JetBrains Educational Licenses](https://www.jetbrains.com/community/education/).
```

### In Spyder (via Anaconda)

Spyder does not natively open `.ipynb` files. The recommended approach is to use **JupyterLab** alongside Spyder, both installed via Anaconda Navigator:

1. Open **Anaconda Navigator**
2. Find **JupyterLab** on the home screen and click **Install** (if not already installed)
3. Once installed, click **Launch** to start JupyterLab in your browser
4. Open and run `.ipynb` notebooks directly in JupyterLab

For working with Python scripts in Spyder, you can use **cell mode** as a notebook-like alternative:

1. Launch **Spyder** from Anaconda Navigator
2. Add `# %%` comments in a `.py` file to define cells
3. Run individual cells with `Ctrl+Enter` or the whole script with `F5`
4. The **IPython console** (bottom-right) shows output interactively

```{tip}
To convert a notebook to a Spyder-compatible Python script:

`jupyter nbconvert --to script notebook.ipynb`

This creates a `.py` file with `# %%` cell markers that Spyder can run cell-by-cell.
```
