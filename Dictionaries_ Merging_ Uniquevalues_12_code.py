# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 09:39:51 2021

@author: User
"""

# 1.	Write a Python program to Extract Unique values dictionary values?

def unique_Values(dic): 
  i=set(dic.values())
  return i

# 2.	Write a Python program to find the sum of all items in a dictionary?

def items_sum(dic): 
  sum_element=0
  for i in dic.values():
    if type(i)==int:
      sum_element+=i
  return sum_element

# 3.	Write a Python program to Merging two Dictionaries?

def merging_Dictionaries(d1,d2):
  for i,j in d2.items():
    d1[i]=j
    return d1


# 4.	Write a Python program to convert key-values list to flat dictionary?




# 5.	Write a Python program to insertion at the beginning in OrderedDict?

def insertion_beginning(dic,upk):
  upk.update(dic)
  print(upk)
  return upk


# 6.	Write a Python program to check order of character in string using OrderedDict()?

from collections import OrderedDict 
def order_of_character(input,check):     
    dic = OrderedDict.fromkeys(input) 
    pattern_count = 0
    for key,value in dic.items(): 
      if (key == check[pattern_count]): 
        pattern_count +=1
      if (pattern_count == (len(check))): 
        return True
    return False


# 7.	Write a Python program to sort Python Dictionaries by Key or Value?
def sort_Dictionaries(dic):
  res=sorted(dic.items())
  return res