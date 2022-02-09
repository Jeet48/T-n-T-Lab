# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:12:13 2022

@author: KIIT
"""

girls = []
boys = []
for i in ['A', 'B', 'C']:
    f = int(input(f"Enter Number of boys in the section {i}: "))
    boys.append(f)
for i in ['A', 'B', 'C', 'D', 'E']:
    f = int(input(f"Enter Number of girls in the section {i}: "))
    girls.append(f)
print(f"Total number of boys: {sum(boys)}")
print(f"Total number of girls: {sum(girls)}")
print(f"Total number of students in the campus: {sum(boys)+sum(girls)}")