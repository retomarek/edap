# Preface

## Book Structure

The book is organized in four main parts:

```{admonition} Part I — Getting Started
:class: hint
Set up your Python environment, learn about Jupyter Notebooks, and install the required packages including [pyedautils](https://pypi.org/project/pyedautils/) and [influxdb-toolkit](https://pypi.org/project/influxdb-toolkit/).
```

```{admonition} Part II — Python Basics
:class: hint
Covers general data analysis tasks: pandas fundamentals, data loading, datetime handling, wrangling, time series operations, exploratory analysis, data quality assessment, and database connectivity with InfluxDB.
```

```{admonition} Part III — Data Visualizations
:class: hint
Brings the numbers to life. Visualization recipes for statistical plots, decompositions, seasonal patterns, heat maps, daily profiles, comfort diagrams, and more — using [Plotly](https://plotly.com/python/) for interactive plots and [pyedautils](https://pypi.org/project/pyedautils/) for energy-domain-specific visualizations.
Each visualization recipe follows a consistent pattern: goal, data basis, data preparation, and visualization. Simply copy the code, run it, and replace the sample data with your own.
```

```{admonition} Part IV — Appendix
:class: hint
Overview of Python packages used in this book and links to additional resources.
```

> *"Numerical quantities focus on expected values, graphical summaries on unexpected values."*
> — John W. Tukey

The recipes show complete workflows from raw data files to final visualizations. Simply copy the code, run it, and replace the sample data with your own.

## Why Python?

In the [EVISU](https://github.com/hslu-ige-laes/evisu) study of the Lucerne University of Applied Sciences and Arts, experts from the field were asked how and where they perform energy analyses. The result: many rely on Excel or building monitoring software.

Excel users are pushing the program to its limits with ever-increasing data sets. Switching to an analysis environment like Python or R seems unavoidable for more complex tasks. However, domain-specific resources have been lacking for the energy and building services engineering industry.

This book is intended to close that gap.

```{tip}
Wondering why Python and not R? I use both! Check out the R version: [Engineering Data Analysis in R](https://hslu-ige-laes.github.io/edar/).
But to be honest, Python is a lot more widespread in the industry...
```

## Acknowledgements

This book was developed using [Jupyter Book](https://jupyterbook.org), an open-source project for building publication-quality books from computational material. The book combines Python code, Jupyter Notebooks, data, and text — all examples are re-executed every time the book is rebuilt.

Hosted on [GitHub Pages](https://pages.github.com). Source available on [GitHub](https://github.com/retomarek/edap).
