# Loading Data

This chapter introduces two functions that can be used to load data from csv- and Excel-files.

## csv-Files
Load data from comma separated files

import pandas as pd

df = pd.read_csv("https://github.com/hslu-ige-laes/edar/raw/master/sampleData/flatElectricity.csv",
                sep = ";")
df.head()