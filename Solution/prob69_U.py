# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:25:47 2019

@author: hoangt1
"""
#Not done: method takes too long, use gdc to check relative prime number
#Note: cannot be prime number
from math import gcd as gcd
def time_this(this):
    def wrapper():
        import time
        t0=time.time()
        retturn_val=this()
        print(time.time()-t0)
        return retturn_val
    return wrapper


@time_this
def run_this():
    max_ratio=0
    for n in range(2,1000000,2): # can only be even number because odd number always has more relatively primes
        count=0
        for j in range(1,n,2): # check with odd numbers only
            if gcd(n,j)==1:
                count+=1
                ratio=n/count
                if ratio<max_ratio: break
            if j==n-1 and ratio>max_ratio:
                max_ratio=ratio
                max_num=n
                print(max_num,max_ratio)
run_this()