# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:12:48 2022

@author: KIIT
"""

money = int(input('Enter money: '))

cost_jeans = money 

additional = ((cost_jeans + 1) * 750) - money

print('Number of jeans that can be brought', cost_jeans)
print('Money required for additional jeans ', additional)