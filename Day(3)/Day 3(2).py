# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 12:23:22 2022

@author: KIIT
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\KIIT\\Data.csv")

counts = [3,3,3]
country = ('France','Germany','Spain')
plt.bar(country,counts,color = ['red','blue','green'])
plt.title('Country count')
plt.xlabel('country')
plt.ylabel('counts')
plt.show()