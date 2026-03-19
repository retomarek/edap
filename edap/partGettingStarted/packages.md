# Python Packages

## Virtual Environments

It is best practice to create a virtual environment for each project. This keeps dependencies isolated and avoids version conflicts.

```bash
# Create a virtual environment
python -m venv .venv

# Activate it
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

```{tip}
VS Code and PyCharm can automatically detect and activate virtual environments.
```

## Installing Packages

Use `pip` to install packages:

```bash
pip install pandas plotly pyedautils influxdb-toolkit
```

Or install all packages used in this book at once:

```bash
pip install -r requirements.txt
```

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
