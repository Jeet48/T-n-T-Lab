# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 13:15:54 2022

@author: KIIT
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\KIIT\\Documents\\Social_Network_Ads.csv")

print(df)

plt.scatter(
        df['Age'],
        df['EstimatedSalary']
        )
plt.title('Graph Ques 6')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')

plt.show()
