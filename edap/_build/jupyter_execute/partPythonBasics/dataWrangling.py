# Data Wrangling
This chapter gives an overview of the most important data manipulation functions used throughout this book.

It is a fact that the data import and manipulation part of analyses often takes more time than the actual analysis or visualization itself. This is because the exchange data formats are not standardized and meters and sensors record at different time intervals. Data quality, missing data, data imputation and data cleansing also play a major role.

# Load data set

import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/retomarek/edap/main/edap/sampleData/flatTempHum.csv",
                 sep = ";")
df.head()

## Access Data

df["FlatA_Temp"]

> Note that a Series is returned

df[["FlatA_Temp", "FlatA_Hum"]]

> Note that a Dataframe is returned

##  Add Metadata for later filtering
Firstly we have to load a dataset into a dataframe