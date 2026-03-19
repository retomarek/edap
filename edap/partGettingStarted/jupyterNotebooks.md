# Jupyter Notebooks

## What are Jupyter Notebooks?

Jupyter Notebooks (`.ipynb` files) are interactive documents that combine code, text, and visualizations. They are the standard format for data analysis in Python and are used throughout this book.

Each notebook consists of **cells**:

- **Code cells** — contain Python code that can be executed
- **Markdown cells** — contain formatted text, headings, lists, images, and equations

## Getting Started

### In VS Code

1. Open a `.ipynb` file or create a new one via `Ctrl+Shift+P` → "Create: New Jupyter Notebook"
2. Select a Python kernel (interpreter) from the top-right dropdown
3. Run cells with `Shift+Enter`

### In JupyterLab

1. Install JupyterLab: `pip install jupyterlab`
2. Start it: `jupyter lab`
3. Create a new notebook from the launcher

### In Google Colab

All notebooks in this book can be opened directly in [Google Colab](https://colab.research.google.com/) using the launch button at the top of each page — no local installation required.

## Useful Shortcuts

| Shortcut | Action |
|---|---|
| `Shift+Enter` | Run cell and move to next |
| `Ctrl+Enter` | Run cell and stay |
| `Esc` then `A` | Insert cell above |
| `Esc` then `B` | Insert cell below |
| `Esc` then `M` | Change cell to Markdown |
| `Esc` then `Y` | Change cell to Code |
| `Esc` then `DD` | Delete cell |

## Cell Tags

This book uses special cell tags to control display:

- `hide-input` — hides the code but shows the output (used for setup cells)
- `output_scroll` — makes long outputs scrollable

```{tip}
In VS Code, you can add cell tags by clicking the gear icon in the cell toolbar.
```
