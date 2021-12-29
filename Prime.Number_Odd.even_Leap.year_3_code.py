# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:41:08 2021

@author: User
"""

# 1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?

x=int(input("Enter the number :"))
if x==0:
    print("entered number =",x," is 0")
elif x<0:
    print("entered number =",x," is negative")
elif x>0:
    print("entered number =",x," is positive")

# 2.	Write a Python Program to Check if a Number is Odd or Even?

x=int(float(input("Enter the number :")))

if x%2==0:
    print("entered number =",x," is even")
else:
    print("entered number =",x," is odd")


# 3.	Write a Python Program to Check Leap Year?

x=int(float(input("Enter the year:")))

if x%4==0 and x%100!=0:
    print("entered year =",x," is a leap year")
else:
    print("entered year =",x," is not a leap year")


# 4.	Write a Python Program to Check Prime Number?

N=int(float(input("Enter the number :")))

if N>1:
    for i in range(2,int(N/2)+1):
        if N%i==0:
            print("Number",N,"is not prime")
            break
    else:
        print("Number",N,"is prime")
else:
    print("Number",N,"is not prime")


# 5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?

l=[]
for j in range(2,10000):
    for i in range(2,int(j/2)+1):
        if j%i==0:
            break
    else:
        l.append(j)
print("All are total:",len(l),"prime number between 1 to 10000 that are:",l)
    
