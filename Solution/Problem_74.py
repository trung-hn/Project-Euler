
#ANSWER: 402
#PROBLEM: Take too long (160 seconds), can fix by reducing the amount of numbers that we alreayd knew will repeat with less than 60 in length

import PremadeTimer,math
import numpy as np
@PremadeTimer.time_this
def calculation(*args):
    counter=0
    for n in range(69,100000):
        # chain_length=fact_chain(n)
        chain=set([n])
        num=n
        while 1:
            # cal fact of each digit and put into list
            lst=[math.factorial(int(d)) for d in str(num)]
            # cal sum using numpy and array
            num=np.sum(np.array(lst))

            # number is repeat
            if num in chain: break
            chain.add(num)

        # if chain length is 60, count
        if len(chain)==60:
            counter+=1
            print(n)
    print(counter)
calculation()


