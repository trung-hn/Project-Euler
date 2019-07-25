# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# 8462696833
import time


def check_prime(i):
    count = 0
    for j in range(2, i / 2):
        if count > 0:
            break
        if i % j == 0:
            count += 1
    if count == 0:
        print i,


number = list()
for i in range(3, 1000000, 2):
    if 600851475143 % i == 0:
        number.append(i)
print number

# Check prime
t0 = time.clock()
for i in number:
    check_prime(i)
