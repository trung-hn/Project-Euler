# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import time

t0 = time.clock()
list_of_prime = [2, ]
for i in xrange(3, 20000, 2):
    Prime = True
    for j in list_of_prime:
        if i % j == 0:
            Prime = False
            break
    if Prime:
        list_of_prime.append(i)
#print list_of_prime[len(list_of_prime) - 1]

#print time.clock() - t0

#print sum(list_of_prime)


def sundaram3(max_n):
    numbers = range(3, max_n + 1, 2)
    half = (max_n) // 2
    initial = 4

    for step in xrange(3, max_n + 1, 2):
        for i in xrange(initial, half, step):
            numbers[i - 1] = 0
        initial += 2 * (step + 1)

        if initial > half:
            return [2] + filter(None, numbers)
t0 = time.clock()
print "Sum of all prime number <2 million is:",sum(sundaram3(2000000))
print time.clock() - t0
