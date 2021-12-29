# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 21:21:48 2021

@author: User
"""

# 1.	Write a Python Program to find sum of array?
arr=[]
arr=[2,4,5,78,887,55,2]
print("Sum of array is : ",sum(arr))


# 2.	Write a Python Program to find largest element in an array?

arr = []
  
# input values to list
arr = [12, 31,578,5, 4, 15,999]
  
g=0
for i in arr:
  if i>g:
    g=i
print ('largest element in an array is',g)

# 3.	Write a Python Program for array rotation?

arr = []
# input values to list
arr = [12, 31,578,5, 4, 15,999] 
arr[:]=arr[::-1]
print('array after rotation is',arr)

# 4.	Write a Python Program to Split the array and add the first part to the end?

def SplitArray(arr, n, k):
	for i in range(0, k):
		x = arr[0]
		for j in range(0, n-1):
			arr[j] = arr[j + 1]
		
		arr[n-1] = x		
arr = [15, 40, 15, 16, 50, 36]
n = len(arr)
position = 2
SplitArray(arr, n, position)
for i in range(0, n):
	print(arr[i], end = ' ')


# 5.	Write a Python Program to check if given array is Monotonic?
def isMonotonic(A):
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1)))
  
# Driver program
A = [6, 5, 44, 4]
  
# Print required result
print(isMonotonic(A))


