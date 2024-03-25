# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 20:57:43 2017

@author: Ching
"""

name=input('Your name: ')
g=int(input('Enter number for male(1) or female(2): '))
h=float(input('Height in cm: '))
we=float(input('Weight in kg: '))
wa=float(input('Waist in cm: '))
#g for gender, h for height
#we for weight, wa for waist

bmi=we/(h/100)**2
fmo=(g==1 and wa<90 or g==2 and wa<80) 
#fmwo= female and male waist okay
fmx=(g==1 and wa>=90 or g==2 and wa>=80) 
#fmx= female and male waist not okay

print("Your BMI is:",format(bmi,' .2f'))
#腰圍可以只看BMI
if (fmo and bmi<18.5):
    print(name,", 您屬於過輕.")
elif (fmo and 18.5<=bmi and bmi<24):
    print(name,", 您屬於健康.")
elif (fmo and 24<=bmi and bmi<27):
    print(name,", 您屬於過重.")
elif (fmo and 27<=bmi and bmi<30):
    print(name,", 您屬於輕度肥胖.")
elif (fmo and 30<=bmi and bmi<35):
    print(name,", 您屬於中度肥胖.")
elif (fmo and 35<=bmi):
    print(name,", 您屬於重度肥胖.")

#腰圍超過
if (fmx):
    print(name,", 因為腰圍超過標準，您的屬於肥胖.") 


