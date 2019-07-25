# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import Premade
import time


def amicable_number(n):
    known_pair = list()
    for i in range(1, n + 1):
        S1 = sum(Premade.multiple_finding(i, True))
        S2 = sum(Premade.multiple_finding(S1, True))
        if i == S2 and i != S1 and i not in known_pair:
            print "Pair of amicable number:", i, S1
            known_pair.extend([i, S1])
    return known_pair


S = amicable_number(10000)
print "The list of all amicable pairs:", S
print "The sum of all amicable numbers under 10000 is:", sum(S)
