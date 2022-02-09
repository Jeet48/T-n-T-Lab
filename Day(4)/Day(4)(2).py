# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 16:10:13 2022

@author: KIIT
"""

Physics = float(input("Please enter Physics score: "))
Chemistry = float(input("Please enter Chemistry score: "))
English = float(input("Please enter English score: "))
Maths = float(input("Please enter Maths score: "))

total = Physics + Chemistry + English + Maths 
average = total / 5
percentage = (total / 500) * 100
 

print("The average mark obtained by student is :",average)
if(average>=90):
    print("The Student got O grade.")
elif(average>=80 and average <90):
    print("The Student got E grade.")
elif(average>=70 and average <80):
    print("The Student got A grade.")
elif(average>=60 and average <70):
    print("The Student got B grade.")
elif(average>=50 and average <60):
    print("The Student got C grade.")
elif(average>=40 and average <30):
    print("The Student got D grade.")
else: 
    print("The Student Failed")