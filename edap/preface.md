# Preface

## Book structure

The book is organized in three main parts:

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

## Why Python?

In the [EVISU study](https://github.com/hslu-ige-laes/evisu), researchers at the Lucerne University of Applied Sciences and Arts asked industry experts how and where they perform energy analyses. The result: many rely either on Excel or on expensive building monitoring applications.

Excel users often push the software to its limits as data volumes continue to grow. Users of monitoring applications, on the other hand, benefit from built-in functionality and visualizations. For more complex tasks, switching to an analysis environment such as Python or R becomes almost inevitable—but the learning curve is steep. At the same time, there have been very few specialist applications to date that are specifically tailored to the field of energy and building services engineering and enable efficient data analysis and visualisation.

This book aims to bridge that gap and make it easier to get started with Python.

```{tip}
Wondering why Python and not R? I use both! Check out the R version: [Engineering Data Analysis in R](https://hslu-ige-laes.github.io/edar/).
But to be honest, Python is much more widely used in the industry...
```

## Acknowledgements

This book is inspired by the [R Graphics Cookbook](https://r-graphics.org/) and [Engineering Data Analysis in R](https://hslu-ige-laes.github.io/edar/).

It was developed using [Jupyter Book](https://jupyterbook.org), an open-source project for building publication-quality books from computational material. The book combines Python code, Jupyter Notebooks, data, and text — all examples are re-executed every time the book is rebuilt.

Hosted on [GitHub Pages](https://pages.github.com). Source available on [GitHub](https://github.com/retomarek/edap).
