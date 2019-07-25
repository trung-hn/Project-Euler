# The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.
# However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2(7830457)+1.
# Find the last ten digits of this prime number.

# NOTE: It's a lot faster if we go through 24 less loops (multiply by 2^24 in each loop) than to go through all loops (multiply by 2 in each loop). Optimal solution would be to find the x where the time to run through loops/x + time to calculate 2^x is optimal (smallest). 
# *Other possible divisor: 509, 614. Time taken: 0.015625

# ANSWER: 8739992577. Time taken:0.046875 (Divisor=24)

import time
initial_time = time.process_time()


def calculation(n):
    number = 28433
    loop_upto = int((n-1)/24)
    for i in range(0, loop_upto):
        number = number * 2**24

        # Multiply by 1 because we minus 1 when we calculate loop_upto
        if i == loop_upto-1:
            number = number*2
        number = number % (10**10)
    number += 1
    return number

print(calculation(7830457))
print("Time taken:", (time.process_time()-initial_time))