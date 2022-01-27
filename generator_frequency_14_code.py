#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Q5 Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
import zlib
s = 'hello world!hello world!hello world!hello world!'.encode()
t = zlib.compress(s)
print("Compressed",t)
print("Decompressed",zlib.decompress(t))


# In[19]:


#Q4 Please write a program to generate all sentences where subject is in ["I", "You"] and 
#verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
x=["I", "You"]
y=["Play", "Love"]
z=["Hockey","Football"]

k=[[i ,j ,k] for i in x for j in y for k in z]
for v in k:
    n=" ".join(v)
    print(n)


# In[2]:


# Question 6:
# Please write a binary search function which searches an item in a sorted list. The function should return the
#index of element to be searched in the list.

import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
bin_search(li,11)


# In[8]:


# Question 1:

# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
class iterator(object):
    def __init__(self, n):
        super(iterator, self).__init__()
        self.n = n
        
    def divBySeven(self):
        for i in range(0, self.n):
            if i % 7 == 0:
                yield i

for num in iterator(250).divBySeven():
    print(num)


# In[10]:


# Question 2:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 

ss = input().split()
word = sorted(set(ss))     # split words are stored and sorted as a set

for i in word:
    print("{0}:{1}".format(i,ss.count(i)))


# In[11]:


# Question 3:Define a class Person and its two child classes: Male and Female. 
# All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

class  Person(object):  
    def  getGender(  self  ):  
        return  "Unknown"  
class  Male(  Person  ):  
    def  getGender(  self  ):  
        return  "Male"  
class  Female(  Person  ):  
    def  getGender(  self  ):  
        return  "Female"  
# Test
aMale  =  Male() 


# In[ ]:




