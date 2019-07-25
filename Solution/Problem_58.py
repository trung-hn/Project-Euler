# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49

# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

# Answer: 26241.0

import time
from Premade2 import check_prime
initial_time=time.process_time()

number_list=[1,3,5,7,9]
def calculation():
    primes_no=3
    for i in range(10,1000000,2):
        length=len(number_list)

        # New number follows this rule
        new_number=number_list[length-4]+i
        number_list.append(new_number)
        
        if check_prime(new_number):
            primes_no +=1
        
        # If condition met, return the length of the side of the cube.
        if primes_no/len(number_list)<0.10:
            return (len(number_list)-1)/2+1 # Minus 1 and then plus 1because of "1" in the middle of the box

print(calculation())
print("Time taken:",time.process_time()-initial_time)
