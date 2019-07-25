# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

# 1: 1
# 3: 1,3
# 6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28

# We can see that 28 is the first triangle number to have over five divisors.

# What is the value of the first triangle number to have over five hundred divisors?
import time
import Premade

list_prime = Premade.prime_sundaram3(300)


def triangle_number(n):
    s = n * (n + 1) / 2
    count = factor_brute_force(s)
    return s, count


def factor_brute_force(n):  # time:4.08577426548
    result = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i == int(n ** 0.5):  # correction for the perfect square
                result += 1
            else:
                result += 2
                # print i,
                # Example: The square root of 18 is 4.2426, rounded up to the next whole number is 5.
                # Testing the integer values 1 through 5 for division into 18 we get these factor pairs: (1 and 18), (2 and 9), (3 and 6).
                # The factors of 18 are 1, 2, 3, 6, 9, 18.
    return result


def factor_prime_method(n):
    count = 0
    remain = 0
    for prime in list_prime[::-1]:
        if prime < n / 2 + 1:
            if n % prime == 0:
                count += 1
                remain = n / prime


t0 = time.clock()
for i in range(1, 100000):
    if triangle_number(i)[1] > 500:
        print "%d is the first number that has more than 500 factor (%d)" % triangle_number(i)
        break
# print factor_brute_force(4123)

print time.clock() - t0