import pandas as pd
import numpy as np
import os


directory = 'csvs'
dfExported = pd.DataFrame()
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        print(f)
        dfExported = dfExported.append(pd.read_csv(f))


dfExported.to_csv('master_export.csv')