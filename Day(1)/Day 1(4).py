# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:43:09 2022

@author: KIIT
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\KIIT\\Documents\\Data.csv")

dataset1 = df.copy(deep=True)

dataset1['Purchased'].replace('No', 0, inplace=True)
dataset1['Purchased'].replace('Yes', 1, inplace=True)


print(pd.crosstab(
        index=dataset1['Purchased'],
        columns = dataset1['Country'],
        dropna=True,
        normalize=True
        ))