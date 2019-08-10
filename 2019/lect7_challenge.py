# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:57:50 2019

@author: work
"""

def factor(num):
    factors=[]
    for k in range(1,num):
        if num%k==0:
            factors.append(k)
    return factors

def printfactor(factors):
    for x in factors:
        print(x)
           
num = input("Please enter the number to be factored:")
if num.isdigit():
     p=factor(int(num))
     print("The factors of ", num)
     printfactor(p)
else:
    print("The entry is not valid")