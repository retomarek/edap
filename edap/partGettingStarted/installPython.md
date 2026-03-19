# Install Python

## Python Installation

Download and install the latest Python version (3.12+) from the official website:

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

An IDE (Integrated Development Environment) helps you write, run, and debug code more efficiently. Two popular choices for Python:

### Visual Studio Code (recommended)

- Free, lightweight, and extensible
- Download: [code.visualstudio.com](https://code.visualstudio.com/)
- Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for syntax highlighting, IntelliSense, and Jupyter support
- Built-in terminal and Git integration

### PyCharm

- Full-featured Python IDE
- Community Edition (free): [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
- Professional Edition includes database tools and web development features

```{tip}
Both VS Code and PyCharm support Jupyter Notebooks directly in the IDE. You do not need to run a separate Jupyter server.
```
