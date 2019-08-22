# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 14:40:11 2019

@author: hoangt1
"""
#ANSWER: 748317
#NOTE: 1 is not prime

def reversed_num(n):
    reversed_n=0
    while(n>0):
        remainder=n%10
        reversed_n=reversed_n*10+remainder
        n=n//10
    return reversed_n

def is_prime(n):
    if n==1: return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return 0
    return 1

def is_truncatable_prime(n):
    if not is_prime(n): return 0

    # right -> left truncation
    n1=n
    n2=n
    while n1>10:
        r2l_trunc=n1//10
        if not is_prime(r2l_trunc):
            return 0
        n1=r2l_trunc
    # left -> right truncation
    while n2>10:
        rev_n=reversed_num(n2)
        l2r_truc=reversed_num(rev_n//10)
        if not is_prime(l2r_truc):
            return 0
        n2=l2r_truc
    return 1

def calculation():
    n=11
    counter=0
    s=0
    while(counter<11):
        n+=2 #Only odd numbers will be checked
        if is_truncatable_prime(n):
            print(n)
            counter+=1
            s+=n
    print(s)

calculation()
