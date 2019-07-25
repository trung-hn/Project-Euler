# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# In combinatorics, we use the notation, 5C3 = 10.

# In general,
# nCr =
# n!
# r!(n−r)!
# 	,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.

# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
# ANSWER: 4075

import math


def calculation(i):
    total = 0
    for n in range(1, i+1):
        for r in range(0, int(n/2)+1):
            C = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
            if C > 1000000:
                if (n == 2*r):
                    total += 1
                else:
                    total += 2
    return total


print("There are %d values that are greater than 1,000,000" %(calculation(100)))
