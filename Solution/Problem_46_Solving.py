# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 9 = 7 + 2×1(2)
# 15 = 7 + 2×2(2)
# 21 = 3 + 2×3(2)
# 25 = 7 + 2×3(2)
# 27 = 19 + 2×2(2)
# 33 = 31 + 2×1(2)
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import math
from Premade2 import check_prime

# Generate Prime number list
prime_list=[2,3,5,7]
def generate_prime(n):
    for i in range(9,n+1,2):
        if check_prime(i):
            prime_list.append(i)

odd_set=set()

def testing(n):
    for odd in range(3,n,2):
        odd_set.add(odd)
        for prime in prime_list:
            if prime > odd:
                break
            root=math.sqrt((odd-prime)/2.0)
            if root.is_integer():
                odd_set.remove(odd)
                break
        if len(odd_set):
            return
generate_prime(100000)
testing(100000)
print(odd_set)