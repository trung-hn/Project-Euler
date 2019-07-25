# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
#  sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
# abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
# the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though
# it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
import time
import Premade

abundant_list = list()


def find_abundant(n):
    for i in range(1, n + 1):
        s = sum(Premade.multiple_finding(i, True))
        if i < s:
            abundant_list.append(i)


def sum_other_numbers(n):
    L = dict()
    for i in range(n):
        L[i] = i
    for x in range(0, len(abundant_list)):
        for y in range(x, len(abundant_list)):
            if abundant_list[x]  + abundant_list[y] > n:
                break
            L[abundant_list[x]+abundant_list[y]] = 0
    return sum(L.values())


t0 = time.clock()
find_abundant(28123)
result = sum_other_numbers(28123)
print"The sum of all positive intergers which can not be written as the sum of two abundant numbers is:", result
print "Time took:", time.clock() - t0
