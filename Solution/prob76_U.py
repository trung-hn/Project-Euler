# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 08:47:47 2019

@author: hoangt1
"""
#Not done
def calculate(n):
    if n==2: return 1
    return calculate(n-1)+n//2


lst=list()
lst.append(0)
for i in range(2,1000000):
    lst.append(lst[-1]+i//2)
#    print(i,lst[-1])
#    print(i,calculate(i))
print(len(lst),lst[-1])