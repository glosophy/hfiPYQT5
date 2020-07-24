import pandas as pd
import numpy as np
import os

cwd = os.getcwd()
print('Current working directory:', cwd)

#Load csv
hfi = pd.read_csv(cwd + '/hfi2019.csv')
print(hfi.head())
print(hfi.dtypes)

#Clean '-' values and coerce score columns to float
hfi = hfi.replace('-', np.nan)
hfi = hfi.replace(' ', np.nan)
hfi.iloc[:,4:] = hfi.iloc[:,4:].apply(pd.to_numeric)

#Save csv
hfi.to_csv(cwd + '/hfi2019CC.csv')