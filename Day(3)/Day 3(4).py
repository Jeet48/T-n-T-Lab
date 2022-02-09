# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 12:57:59 2022

@author: KIIT
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\KIIT\\Social_Network_Ads.csv")

plt.scatter(df['Age'],df['EstimatedSalary'],c='blue')
plt.show()