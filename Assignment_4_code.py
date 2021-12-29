# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 15:27:33 2021

@author: User
"""

# 1.	Write a Python Program to Find the Factorial of a Number?
a=int(input("Enter number : "))
k=1
for i in range(1,a):
  k=k*i
print("Factorial of ",a,"is",k)

# 2.	Write a Python Program to Display the multiplication Table?

num=int(input("Enter number : "))
for i in range(1,11):
  print(num,"X",i,"=",num*i)

# 3.	Write a Python Program to Print the Fibonacci sequence?

num=int(input("Enter the num:"))
a=0
b=1
count=0
if num<0:
  print("Invalid num")
elif num==0:
  print("0")
elif num==1:
  print("1")
else:
  print("Fibonacci sequence:")
  while count<num:
    print(a)
    c=a+b
    b=a
    a=c
    count+=1

# 4.	Write a Python Program to Check Armstrong Number?

num = int(input("Enter a number: "))

# initialize sum
sum = 0
k=len(str(num))
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** k
    temp=temp//10

# display the result
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")

# 5.	Write a Python Program to Find Armstrong Number in an Interval?

lower = int(input("Enter a lower range: "))
upper = int(input("Enter a upper range: "))

for i in range(lower,upper+1):
  # initialize sum
  sum = 0
  k=len(str(i))
  temp = i
  while temp > 0:
    digit = temp % 10
    sum += digit ** k
    temp=temp//10

  # display the result
  if i == sum:
    print(i,"is an Armstrong number")

# 6.	Write a Python Program to Find the Sum of Natural Numbers?
n = int(input("Enter n: "))
s=int((n*(n+1))/2)
print("Sum of first",n,"natural numbers are: ",s)
