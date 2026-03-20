# Energy Data Analysis with Python (EDAP)

[![Deploy Book](https://github.com/retomarek/edap/actions/workflows/deploy.yml/badge.svg)](https://github.com/retomarek/edap/actions/workflows/deploy.yml)
[![Jupyter Book](https://img.shields.io/badge/Jupyter%20Book-v1-orange?logo=jupyter)](https://jupyterbook.org)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

An interactive online book for analyzing and visualizing energy and comfort time series data with Python.

**Read the book: [retomarek.github.io/edap](https://retomarek.github.io/edap/)**

## Contents

- **Getting Started** - Python installation and environment setup
- **Python Basics** - Data loading, metadata, wrangling, EDA, and time series analysis
- **Data Visualizations** - Recipes for common energy and comfort plots

## Local Development

```bash
# Clone the repository
git clone https://github.com/retomarek/edap.git
cd edap

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Build the book
jupyter-book build edap
```

After the build completes, open the book in your browser:

```bash
# macOS / Linux
open edap/_build/html/index.html

# Windows (Command Prompt)
start edap\_build\html\index.html

# Windows (PowerShell)
Invoke-Item edap\_build\html\index.html

# Or paste this path directly into your browser
# file:///path/to/edap/edap/_build/html/index.html
```

### Build Scripts (Windows)

- **`build.bat`** — Builds the book (fast, uses cache). Then open `edap/_build/html/index.html` in the browser and refresh with F5.
- **`build-clean.bat`** — Cleans the cache and rebuilds everything (use after config or logo changes, takes a few minutes).

### Rebuild After Changes

Run `jupyter-book build edap` (or double-click `build.bat`) after making changes, then refresh the browser with F5. Jupyter Book caches executed notebooks, so only changed pages are re-built.

To force a clean rebuild (re-executes all notebooks):

```bash
jupyter-book clean edap
jupyter-book build edap
```

## Deployment

The book is automatically built and deployed to GitHub Pages via GitHub Actions on every push to `main`. See the [workflow](.github/workflows/deploy.yml) for details.

## License

This project is licensed under the [GNU General Public License v3](LICENSE).

## Credits

Built with [Jupyter Book](https://jupyterbook.org/).
