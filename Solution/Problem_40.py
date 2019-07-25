# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
# ANSWER: 210

import time

initial_time = time.process_time()
list_of_digit= list()
k=1
def calculation(n):
    global k
    for i in range(1,n):
        for digit in str(i):
            # Append every digit of a number
            list_of_digit.append(int(digit))
            # Return at kth value
            if k >=n:
                return
            k+=1
# Generate an array upto 1000000th value
calculation(1000000)
product = 1

# Take the product of the value at these positions
for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    product = product*list_of_digit[i-1]
print("The product of all the digits at 1,10,...,1000000 is %d" %(product))
print("\nTime taken %f" % (time.process_time()-initial_time))
