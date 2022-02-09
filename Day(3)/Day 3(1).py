# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 12:08:10 2022

@author: KIIT
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\KIIT\\Social_Network_Ads.csv")


plt.hist(df['EstimatedSalary'],
         color = 'blue',
         edgecolor = 'white',
         bins = 4);
plt.title('Histogram of salary')

plt.show()