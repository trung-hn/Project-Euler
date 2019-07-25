#%%
from decimal import *
import math
#%%
def calculation(*args):
    getcontext().prec=100 #100 decimal places
    total=0
    for n in range(101):
        decimal_place=Decimal(n).sqrt()
        lst=[int(d) for d in str(decimal_place)[2:]]
        # if str(decimal_place)[-1]!="0":
        print(sum(lst))
        total+=sum(lst)
        # if lst[-1]==0:
        #     print(n)
    print(total)
calculation()


#%%
