# The following iterative sequence is defined for the set of positive integers:

# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.
import time

known = {1: 1, 2: 2, 4: 3, }  # known count for each natural number


def count_until_one(n):
    highest, index = 0, 0
    for i in range(1, n):
        j, count = i, 0
        while (j != 1):
            if j in known:
                count += known[j]
                break
            if j % 2 == 0:
                j = j / 2
            else:
                j = 3 * j + 1
            count += 1
        known[i] = count
        if count > highest:
            highest, index = count, i
    print "Number %d has the longest chain of %d" % (index, highest)


t0 = time.clock()
count_until_one(1000000)
print "Time took:", time.clock() - t0
