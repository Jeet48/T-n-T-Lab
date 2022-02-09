# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 13:23:41 2022

@author: KIIT
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\KIIT\\Documents\\Data.csv")

sal_class = []

for i in range(10):
    
    sal = df['Salary'][i]
    
    if sal>70000:
        sal_class.append('class0')
    elif sal>=61000:
        sal_class.append('class1')
    elif sal >= 48000:
        sal_class.append('class2')
    else:
        sal_class.append('')

df['Salary_class'] = sal_class

print(df)