# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:11:45 2022

@author: KIIT
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\KIIT\\Social_Network_Ads.csv")

sns.distplot(df['Age'],kde=False)
