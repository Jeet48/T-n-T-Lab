# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:43:17 2022

@author: KIIT
"""


import pandas as pd

df = pd.read_csv("C:\\Users\\KIIT\\Documents\\Data.csv")

dataset1 = df.copy(deep=True)

print(dataset1)

