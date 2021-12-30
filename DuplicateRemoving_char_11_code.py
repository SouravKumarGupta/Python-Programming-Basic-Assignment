# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 21:40:34 2021

@author: User
"""

# 1.	Write a Python program to find words which are greater than given length k?
st = "hello geeks for geeks is computer science portal" 
k = 4
test=[]
for i in st.split():
  if len(i)>k:
    test.append(i)
print("words which are greater than given length", k,"are",test)



# 2.	Write a Python program for removing i-th character from a string?
#j=i-th character from a string which want to remove
def remove_char(string,j):
  word=string[:j]+string[j+1:]
  return word

# 3.	Write a Python program to split and join a string?

def split_join(string):
  for i in string.split():
    strjoined="".join(i)
  return strjoined

# 4.	Write a Python to check if a given string is binary string or not?

def isBinary(num):
    for i in str(num):
        if i not in ("0","1"):
            return False
    return True


# 5.	Write a Python program to find uncommon words from two Strings?

def uncommon_words(a,b): 
  uncommon_words_res=""
  for j in b.lower():
    if j not in a.lower():
      uncommon_words_res=uncommon_words_res+j
  return uncommon_words_res


# 6.	Write a Python to find all duplicate characters in string?

def duplicate_characters(string): 
  temp=""
  for j in string:
    if string.count(j)>1:
      temp+=j
  return set(temp)


# 7.	Write a Python Program to check if a string contains any special character?
def special_characters(string): 
  if string.isalnum():
    return True
  return False