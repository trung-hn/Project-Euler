# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
# ANSWER: 669171001

number_list = [1, 3, 5, 7, 9]


def calculation():
    for i in range(10, 10000, 2):
        length = len(number_list)

        # New number follows this rule
        number_list.append(number_list[length-4]+i)

        # Each side of the cube is 1001 long.
        if len(number_list) == 2001:
            return


calculation()
print("The sum of all elements on the diagonals is: ", sum(number_list))
