# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 13:46:02 2019

@author: hoangt1
"""
#Answer: 127035954683=5027**3=8384**3
D={}
for i in range(10000):
    cube=i**3
    lst=list(str(cube))
    lst.sort()
    D[cube]=lst

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
    for i,ivalue in enumerate(D.values()):
        count=0
        for j,jvalue in enumerate(D.values()):
            if j<=i: continue # already check in previous loops
            if j>i*2.16:break #cube root of 10. We know that these will never equal
            if ivalue==jvalue:
                count+=1
            if count==4:
                return i

i=run_this()
print(i,i**3)