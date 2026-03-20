# Jupyter Notebooks

## What are Jupyter Notebooks?

Jupyter Notebooks (`.ipynb` files) are interactive documents that combine code, text, and visualizations. They are the standard format for data analysis in Python and are used throughout this book.

Each notebook consists of **cells**:

- **Code cells** — contain Python code that can be executed
- **Markdown cells** — contain formatted text, headings, lists, images, and equations

## Using Google Colab

[Google Colab](https://colab.research.google.com/) is a free, cloud-based Jupyter environment — no local installation required.

**Opening notebooks from this book in Colab:**

The notebooks in this book that are based on `.ipynb` files can be opened directly in Google Colab. On those pages, a rocket icon ({fa}`rocket`) appears in the top toolbar — click it and select **Colab** to open the notebook there.

```{admonition} Note
:class: warning
The launch button only appears on pages that are based on `.ipynb` notebook files, not on regular text pages like this one. Try it on one of the notebook pages, e.g. in the [Python Basics](../partPythonBasics/pandasIntro) section.
```

```{tip}
**Try Jupyter without installing anything!** You can explore Jupyter Notebooks directly in your browser using the official Jupyter demo:

[jupyter.org/try-jupyter — Interactive Intro Notebook](https://jupyter.org/try-jupyter/notebooks/?path=notebooks/Intro.ipynb)

This opens a fully functional JupyterLab environment with an introductory notebook — perfect for a first look at how notebooks work before setting up a local environment.
```

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
For local Jupyter Notebook usage in VS Code, PyCharm, Spyder, or JupyterLab, see the [Python Installation & IDE Setup](../appendix/installPython) appendix.
```
