# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:36:43 2019

@author: hoangt1
"""
#Answer:9110846700
s=0
for i in range(1,1001):
    s+=i**i
    if len(str(s))>10:
        s=int(str(s)[-10:])
    print(s)