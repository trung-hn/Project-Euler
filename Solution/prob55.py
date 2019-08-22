# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:25:29 2019

@author: hoangt1
"""
#ANSWER: 249

def flip_number(number):
    new_num=0
    while number >0:
        remainder=number%10
        new_num=new_num*10+remainder
        number=number//10
    return new_num

count=0
for i in range(10000):
    start_num=i
    for j in range(50):
        num=start_num+flip_number(start_num)
        if num==flip_number(num):
            break
        start_num=num
    else:
        count+=1

print(count)

#Prime related probs: 60

