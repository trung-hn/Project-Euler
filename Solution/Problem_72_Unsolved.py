
#APPROACH: count relatively prime pairs
#PROBLEM: takes too long

import PremadeTimer,math

#Count relatively prime pairs
@PremadeTimer.time_this
def prob72(*args):
    counter=0
    for d in range(1001):
        for n in range(d):
            if math.gcd(n,d)==1:
                counter+=1
    return counter

#Use set
@PremadeTimer.time_this
def prob72_2(*args):
    s=set()
    for d in range(1001):
        for n in range(d):
            s.add(n/d)
    return s

print(prob72())
print(len(prob72_2()))