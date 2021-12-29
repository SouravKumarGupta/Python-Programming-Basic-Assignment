# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 18:43:07 2021

@author: User
"""

# 1.	Write a Python Program to Find LCM?

x = int(input("Enter 1st no: "))
y = int(input("Enter 2nd no: "))
z=max(x,y)
while(True):
  if z%x==0 and z%y==0:
    LCM=z
    break
  z+=1
print("LCM of",x,"&",y,"is",LCM)

# 2.	Write a Python Program to Find HCF?
x = int(input("Enter 1st no: "))
y = int(input("Enter 2nd no: "))
for i in range(1,min(x,y)+1):
  if x%i==0 and y%i==0:
    HCF=i
print("HCF of",x,"&",y,"is",HCF)


# 3.	Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
dec=int(input("Enter decimal value:"))
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

# 4.	Write a Python Program To Find ASCII value of a character?

character=input("Enter character:")
print("ASCII value of a character",character,"is",ord(character))

# 5.	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

x = int(input("Enter 1st no: "))
y = int(input("Enter 2nd no: "))
res=int(input("Pls enter for Addition=1 Substraction=2 Multiplication=3 Division=4 :"))
if res==1:
  print("Addition of",x,"&",y,"is",x+y)
elif res==2:
  print("Substraction of",x,"&",y,"is",x-y)
elif res==3:
  print("Multiplication of",x,"&",y,"is",x*y)
elif res==4:
  print("Division of",x,"&",y,"is",x/y)


