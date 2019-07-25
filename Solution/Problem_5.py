# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

for i in range(27720, 10000000000, 27720):
    count = 0
    for j in range(1, 21):
        if i % j == 0:
            count += 1
        else:
            break
    if count == 20:
        print "The Smallest number that is evenly divisible by all of the numbers from 1 to 20 is:",i
        break

        # 20 = 2^2 * 5
        # 19 = 19
        # 18 = 2 * 3^2
        # 17 = 17
        # 16 = 2^4
        # 15 = 3 * 5
        # 14 = 2 * 7
        # 13 = 13
        # 11 = 11
        # All others are included in the previous numbers.
        # ANSWER: 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232 792 560