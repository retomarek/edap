# Python Packages

## Virtual Environments

It is best practice to create a virtual environment for each project. This keeps dependencies isolated and avoids version conflicts.

First, create a project folder and navigate into it:

```bash
mkdir my-project
cd my-project
```

Then create and activate a virtual environment inside that folder:

```bash
# Create a virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

The `.venv` folder contains the isolated Python installation. All packages you install with `pip` while the environment is active are stored there.

```{tip}
VS Code and PyCharm can automatically detect and activate virtual environments.
```

:::{admonition} Anaconda
:class: note
Anaconda uses its own environment system (`conda`) instead of `venv`. You can create environments via **Anaconda Navigator** (Environments tab) or via the command line:

```bash
conda create -n my-project python=3.12
conda activate my-project
```

Do not mix `venv` and `conda` — use one or the other. If you installed Python via Anaconda, use `conda` environments.
:::

## Installing Packages

Use `pip` to install packages:

```bash
pip install pandas plotly pyedautils influxdb-toolkit
```

Or install all packages used in this book at once:

```bash
pip install -r requirements.txt
```

:::{admonition} Anaconda users — use conda instead of pip!
:class: warning
If you are using **Anaconda**, always install packages via **Anaconda Navigator** or `conda install` instead of `pip`:

```bash
conda install pandas plotly statsmodels
```

Mixing `pip` and `conda` in the same environment can lead to broken dependencies — `conda` manages packages differently than `pip`, and installing with `pip` can overwrite or conflict with `conda`-managed packages. This may result in import errors, version mismatches, or a corrupted environment that needs to be recreated.

If a package is not available via `conda` (e.g. `pyedautils`), install it with `pip` as a last resort, but do so **after** all `conda` packages are installed.
:::

## Key Packages

| Package | Purpose |
|---|---|
| [pandas](https://pandas.pydata.org/) | Data manipulation and analysis |
| [numpy](https://numpy.org/) | Numerical computing |
| [plotly](https://plotly.com/python/) | Interactive visualizations |
| [matplotlib](https://matplotlib.org/) | Static visualizations |
| [pyedautils](https://pypi.org/project/pyedautils/) | Energy data analysis utilities — ready-to-use visualization functions |
| [influxdb-toolkit](https://pypi.org/project/influxdb-toolkit/) | Connect to InfluxDB v1/v2 time series databases |
| [statsmodels](https://www.statsmodels.org/) | Time series decomposition and statistics |
| [kaleido](https://github.com/plotly/Kaleido) | Static image export for Plotly |

## Updating Packages

```bash
pip install --upgrade pyedautils
```
