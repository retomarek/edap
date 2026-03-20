# Part III — Data Visualizations

In the following chapters, visualizations are presented that are frequently used in the field of building energy monitoring. Sometimes not the visualization itself is challenging, but the preceding data preparation. Therefore, all recipes show the complete workflow from raw data to final plot.

## Plotly and pyedautils

All visualizations in this book use [Plotly](https://plotly.com/python/) for interactive plots — every chart is zoomable, hoverable, and exportable. Many recipes use [pyedautils](https://pypi.org/project/pyedautils/), a Python package that provides ready-to-use visualization functions for energy data analysis.

## Recipe Pattern

Each visualization notebook follows a consistent structure:

```{admonition} Goal
:class: tip
What the visualization shows and when to use it.
```

```{admonition} Data Basis
:class: note
Which data is needed — format, columns, and resolution.
```

**Data Preparation** — Load and transform the raw data.

**Visualization** — Create the plot using pyedautils or manual Plotly code.

```{dropdown} Customization
Optional parameters for colors, labels, and layout.
```

## Categories

The visualizations are organized into the following categories:

- **Statistical** — Boxplots, density plots, cross-correlations
- **Decomposition** — Long-term and short-term time series decomposition
- **Seasonal** — Overlapping years, miniplots, polar charts, before/after comparisons
- **Heat Maps** — Calendar heat maps and median week patterns
- **Daily Profiles** — Overview, overlayed, mean, and decomposed profiles
- **Sum & Frequency** — Daily and hourly aggregations
- **Comfort** — Temperature-humidity, Mollier h-x, SIA 180 diagrams
- **Miscellaneous** — Energy signatures, household electricity, multi-axis plots
