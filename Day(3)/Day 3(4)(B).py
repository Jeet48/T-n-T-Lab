# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 12:44:52 2022

@author: KIIT
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\KIIT\\Social_Network_Ads.csv")

sns.set(style="darkgrid")
sns.regplot(x=df['Age'], y=df['EstimatedSalary'],fit_reg=False)