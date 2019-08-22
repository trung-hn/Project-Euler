# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:15:38 2019

@author: hoangt1
"""
# Answer:428570
# Note: it is important to make the boundaries of n dynamic to decrease run time.
# We know ratio is restricted by 3/7 (upper bound) and optimal_ratio(lower bound, dynamic)
# Assign these bounds to n, we can reduce time significanly (by thounsands times)

import math
def time_this(func):
    def wrapper():
        import time
        t0=time.time()
        return_val=func()
        print(time.time()-t0)
        return return_val
    return wrapper

@time_this
def run_this():
    optimal_d=0
    optimal_n=0
    optimal_ratio=0
    for d in range(1000000):
        for n in range(math.floor(optimal_ratio*d), math.ceil(3/7*d)):
            ratio=n/d
            if optimal_ratio< ratio and ratio<3/7:
                optimal_ratio=ratio
                optimal_d=d
                optimal_n=n
    return optimal_n,optimal_d
n,d=run_this()
print(n/math.gcd(n,d))
