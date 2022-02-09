# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:22:32 2022

@author: KIIT
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\KIIT\\Data.csv")

sns.countplot(x="Country",data=df, hue="Purchased")
