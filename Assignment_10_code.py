# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 15:45:51 2021

@author: User
"""

# 1.	Write a Python program to find sum of elements in list?

# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
  ele = int(input())
  lst.append(ele) # adding the element
print("sum of elements in list",lst,"is",sum(lst))

# 2.	Write a Python program to  Multiply all numbers in the list?

# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
  ele = int(input())
  lst.append(ele) # adding the element
mulp=1
for i in range(len(lst)):
  mulp=mulp*lst[i]
print("product of elements in list",lst,"is",mulp)

# 3.	Write a Python program to find smallest number in a list?

# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
  ele = int(input())
  lst.append(ele) # adding the element
print("smallest number in a list",lst,"is",min(lst))


# 4.	Write a Python program to find largest number in a list?

# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
  ele = int(input())
  lst.append(ele) # adding the element
lst.sort()
print("largest number in a list",lst,"is",lst[-1])


# 5.	Write a Python program to find second largest number in a list?

# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
  ele = int(input())
  lst.append(ele) # adding the element
lst.sort()
print("2nd largest number in a list",lst,"is",lst[-2])


# 6.	Write a Python program to find N largest elements from a list?

# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
  ele = int(input())
  lst.append(ele) # adding the element
lst.sort()
N = int(input("Enter N largest elements which you want from a list : "))
try:
  if N<=len(lst):
    print(N,"largest number in a list",lst,"is",lst[-N])
except:
  print("Pls enter valid no")

# 7.	Write a Python program to print even numbers in a list?
# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
  ele = int(input())
  lst.append(ele) # adding the element
e=[]
e=[num for num in lst if num%2==0]
print("even numbers in a list",lst,"is",e)


# 8.	Write a Python program to print odd numbers in a List?

# creating an empty list
lst = []
# number of elements as input
n = int(input("Enter number of elements : "))
# iterating till the range
for i in range(0, n):
  ele = int(input())
  lst.append(ele) # adding the element
e=[]
e=[num for num in lst if num%2!=0]
print("odd numbers in a list",lst,"is",e)

# 9.	Write a Python program to Remove empty List from List?

test_list = [5, 6, [], 3, [], [], 9]
e=[num for num in test_list if num!=[]]
print("Final list after remove empty List from List",e)

# 10.	Write a Python program to Cloning or Copying a list?

test_list = [5,6,3,9]
new_list=test_list[:]
print("New list after copy",new_list)

# 11.	Write a Python program to Count occurrences of an element in a list?
test_list = [3,5,6,3,6,9,3]
for i in set(test_list):
  print("Count of occurrences of",i,"is",test_list.count(i))