#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:28:45 2020

@author: samadhan
"""

def area(type__ ,x):
    if type__ =="circle":
        area=3.14*x**2
        print("Area of circle is :", area)
    elif type__=="square":
        area=x**2
        print("Area of square is  :",area)
    else:
        print("I don't know that one !!!!!!!  ")
        