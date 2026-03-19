# Install Python

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
- ⚠️ Requires some setup — not ready out of the box for Python

### Spyder
**Best for:** Data analysis, scientific computing, and beginners coming from MATLAB
- Free and open-source: [spyder-ide.org](https://www.spyder-ide.org/)
- Ships ready-to-use with Anaconda — minimal setup required
- Variable explorer lets you inspect data like in Excel; integrated IPython console and plot viewer
- ⚠️ Limited support for non-scientific or larger software projects

### PyCharm
**Best for:** Larger Python projects, software engineering, and teams
- Community Edition (free): [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
- Powerful refactoring tools, built-in debugger, and project-wide code navigation
- Professional Edition adds database tools and web development (Django, FastAPI) features
- ⚠️ Heavier on system resources; more features than beginners may need


```{tip}
**Not sure which to pick?** Start with **Spyder** (via Anaconda) if your focus is data analysis and you do not have already VS Code.
Choose **VS Code** if you want flexibility and plan to do more than just Python.
Go with **PyCharm** if you're building larger applications or working in a team.

Both VS Code and PyCharm support Jupyter Notebooks directly in the IDE — no separate Jupyter server needed. Spyder via Anaconda also includes a Jupyter server.
```