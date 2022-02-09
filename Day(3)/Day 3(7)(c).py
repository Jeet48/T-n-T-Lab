# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:24:48 2022

@author: KIIT
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\KIIT\\Data.csv")

sns.boxplot(x=df['Age'], y=df['Country'])