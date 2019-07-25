# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
import time
t0=time.clock()
list_of_prime=[2]
for i in range(3, 200000,2):
    count = 0
    for j in list_of_prime:
        if i % j == 0:
            count += 1
            break
    if count == 0:
        list_of_prime.append(i)
    if len(list_of_prime)>10001:
        break
print "The 10 001st prime number is",list_of_prime[10000]
print time.clock()-t0

