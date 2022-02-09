# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:56:22 2022

@author: KIIT
"""

import pandas as pd


dataset=pd.read_csv("C:\\Users\\KIIT\\Documents\\Data.csv")
print("\nDataset given")
print(dataset)
dataset.select_dtype_counts()