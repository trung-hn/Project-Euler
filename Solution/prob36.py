# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:04:38 2019

@author: hoangt1
"""
#ANSWER: 872187
#APPROACH: check palindromic for nunber then check for number in binary format.

def reversed_num(n):
    reversed_n=0
    while(n>0):
        remainder=n%10
        reversed_n=reversed_n*10+remainder
        n=n//10
    return reversed_n

def check_palindromic(n):
    if n==reversed_num(n):
        return 1
    return 0

def time_this(func):
    def timer():
        import time
        t0=time.time()
        re=func()
        print(time.time()-t0)
        return re
    return timer

@time_this
def calculation():
    s=0
    for n in range(1000000):
#        check_palindromic(n)
        if check_palindromic(n):
            num_bin=int("{0:b}".format(n))
            if check_palindromic(num_bin):
                s+=n
    return s


print(calculation())
