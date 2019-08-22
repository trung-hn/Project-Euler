# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 13:41:40 2019

@author: hoangt1
"""
# ANSWER: 55
# APPROACH: break programs into check_is_cir_prime -> check_prime

def is_prime(n):
    if n==1: return 0
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return 0
    return 1

def is_circular_prime(n):
    # rotate length(n) amount or rotations
    n_length=len(list(str(n)))
    for i in range(n_length):
        # check prime for each rotation
        if not is_prime(n): return 0
        #rotate
        right_most_digit=n%10
        n=n//10+10**(n_length-1)*right_most_digit
    # only prime gets here
    return 1

known_cir_prime=set([2])
def calculation():
    for n in range(3,1000000,2):
        # known circular_prime
        if n in known_cir_prime: continue

        # else check
        if is_circular_prime(n):
            #if prime, add to knowdb. reduce time for further number
            known_cir_prime.add(n)

calculation()
print(known_cir_prime)
print(len(known_cir_prime))