# Counting fractions in a range
# Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# It can be seen that there are 3 fractions between 1/3 and 1/2.
# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?



#APPROACH: adjust range of n 
#NOTE: gcd method won't work because there are unexpected case
#ANSWER: 7295372

import PremadeTimer,math

#Count relatively prime pairs
@PremadeTimer.time_this
def calculation(*args):
    s=set()
    for d in range(12001):
        for n in range(math.floor(1/3*d),math.ceil(1/2*d)):
            # if math.gcd(n,d)==1:
            #     counter+=1
            if n/d>1/3 and n/d<1/2:
                s.add(n/d)
    return len(s)
print(calculation())