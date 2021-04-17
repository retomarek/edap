# Explorative Data Analysis
Explorative Data Analysis (EDA) is a technique based on the human characteristic of visual pattern recognition.

The purpose of EDA is simple: learn more about data by visualizing it in different ways.

> “Exploratory data analysis is graphical detective work.” - John W. Tukey, considered the founder of EDA

## Get Overview of Data
A first step is getting an overview of the whole data set and specific series of it.

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/retomarek/edap/main/edap/sampleData/flatTempHum.csv",
                 sep = ";")

df

df.head(3)

df.tail(2)

df.shape

df.dtypes

```{note}
The type "object" normally points to unclean data, e.g. the time which should be a datetime object
```

## Names

df.columns

## Descriptive Statistics

df.describe()

df.describe(include="all")

df["FlatA_Temp"].min()

df["FlatA_Temp"].max()

df["FlatA_Temp"].median()

df["FlatA_Temp"].mean()

df["FlatA_Temp"].hist()