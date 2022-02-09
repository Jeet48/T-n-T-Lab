# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:10:54 2022

@author: KIIT
"""

person_age=input(" What is your age ")
if(int(person_age)>65):
    print("The person has already reired")
else:
    print("The person have",65-int(person_age),"years late before retirement")