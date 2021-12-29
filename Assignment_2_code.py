# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 20:55:41 2021

@author: User
"""

# # #1.	Write a Python program to convert kilometers to miles?
# km=float(input("Enter value in kilometer : "))
# # 1km=0.6213 miles
# m=0.6213

# print(round(km*m,2),"Miles")

# # #2.	Write a Python program to convert Celsius to Fahrenheit?
# celsius=float(input("Enter the value in celsius : "))
# # calculate fahrenheit
# fahrenheit = (celsius * 1.8) + 32
# print(fahrenheit,"fahrenheit")

# #3.	Write a Python program to display calendar?
# import calendar
# yy=2021
# print(calendar.calendar(yy))

#4.	Write a Python program to solve quadratic equation?
import cmath,math
a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
d=(b**2)-(4*a*c)
if d==0:
    r1=(-b/(2*a))
    print("Roots are real and equal : ",r1)
elif d<0:
    s1=(-b+cmath.sqrt(d))/2*a
    s2=(-b-cmath.sqrt(d))/2*a
    print("Roots are complex :",s1,s2)
else:
    s1=(-b+math.sqrt(d))/2*a
    s2=(-b-math.sqrt(d))/2*a
    print("Roots are real and distinct :",s1,s2)

#5.	Write a Python program to swap two variables without temp variable?
# x=input("Enter 1st value : ")
# y=input("Enter 2nd value : ")

# x,y=y,x

# print("Reveresd values are : ",x,y)
