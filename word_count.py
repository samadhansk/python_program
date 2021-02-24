#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 19:04:54 2020

@author: samadhan
"""

#program for counting the number of word in the string


str1=input("Enter the string :")
word=input("Enter the word to be search in the string  :")
list1=str1.split()
count=0
print(list1)
for w in list1:
    if w==word:
        count=count +s
        
        
print("The word are present  time in string",count)