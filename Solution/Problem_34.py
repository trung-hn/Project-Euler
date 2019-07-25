# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.
# ANSWER: 40730
from scipy.special import factorial
import math
import time
start_time = time.time()


def calculation(n):
    final_sum = 0
    for i in range(10, n):
        sum = 0
        # sum of digits
        for digit in str(i):
            sum = sum + math.factorial(int(digit))
        # sum of digits = number
        if sum == i:
            final_sum += i
    return final_sum


print("Sum is", calculation(500000))
print("%s seconds" % (time.time()-start_time))
