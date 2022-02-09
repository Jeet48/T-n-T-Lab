# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:17:35 2022

@author: KIIT
"""

n = int(input('Enter the number: '))

c = 0

for i in range(2, n):
    if n%i == 0:
        c += 1
        break

if c != 0:
    print('It is not a prime number')
else:
    print('It is a Prime number')
