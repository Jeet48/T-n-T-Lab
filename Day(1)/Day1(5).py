# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:44:12 2022

@author: KIIT
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\KIIT\\Documents\\Data.csv")

dataset1 = df.copy(deep=True)

dataset1['Purchased'].replace('No', 0, inplace=True)
dataset1['Purchased'].replace('Yes', 1, inplace=True)

coun = np.array(dataset1['Country'].unique())

for n, i in enumerate(coun):
    dataset1['Country'].replace(i, n, inplace=True)



print(dataset1.corr())
