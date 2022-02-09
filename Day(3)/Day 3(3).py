# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 12:26:21 2022

@author: KIIT
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\KIIT\\Data.csv")

df.dropna(axis = 0, inplace=True)
print(np.shape(df))
