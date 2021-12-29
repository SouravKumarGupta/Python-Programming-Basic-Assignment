# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 19:44:36 2021

@author: User
"""
#1.	Write a Python program to print "Hello Python"?
print("Hello Python")

#2.	Write a Python program to do arithmetical operations addition and division.?
a=10
b=5
print("Sum is ",a+b)
print("Division is",a/b)

#3.	Write a Python program to find the area of a triangle?
a,b,c=11,12,13
#Uncomment to take user input
#a=float(input("Enter the 1st side: "))
#b=float(input("Enter the 2nd side: "))
#c=float(input("Enter the 3rd side: "))

#calculate the semi perimeter
s=(a+b+c)/2


#calculate the area
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of Triangle is %0.3f"%area)

#4.	Write a Python program to swap two variables?
a=12
b=21
c=a
a=b
b=c
print("After swap" " a=",a,"& b=",b)

#5.	Write a Python program to generate a random number?
#Generate a random no between 0 and 9
import random
print("Random no between 0 and 9 is",random.randint(0,9))

