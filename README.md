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
jupyter-book build edap/

# Open in browser
open edap/_build/html/index.html
```

## Deployment

The book is automatically built and deployed to GitHub Pages via GitHub Actions on every push to `main`. See the [workflow](.github/workflows/deploy.yml) for details.

## License

This project is licensed under the [GNU General Public License v3](LICENSE).

## Credits

Built with [Jupyter Book](https://jupyterbook.org/).
