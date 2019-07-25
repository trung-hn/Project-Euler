# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
number_list = list()


def list_number(n):
    # Initial the digit dictionary
    D = dict()
    for digit in range(0, n):
        D[digit] = digit

    # List all possible cases
    for i in range(0, n):
        for move_digit in range(n - 1, 0, -1):  # the last digit will move forward to the first place

            # combining all digits and add to another list
            number = ""
            for spot in range(0, n):
                number += str(D[spot])
            number_list.append(number)

            # the replace digit
            be_moved_di = move_digit - 1
            # Move digit
            D[move_digit], D[be_moved_di] = D[be_moved_di], D[move_digit]


# number_list.sort()
def find_smallest_factor():
    known_digits = list()
    upper_limit = 1000000
    natural_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for digit in range(0, 10):

        # Calculate the factorial of other digits up to this point(digit)
        product = 1
        for i in range(1, 10 - digit):
            product = product * i

        # Calculate largest factor
        factor = upper_limit / product

        # We need to have a remainder for the next case
        if upper_limit % product == 0:
            factor -= 1

        # Value equals the value at location factor in the list
        value = natural_number[factor]

        # Delete the value in the natural number list
        natural_number.remove(value)

        #Change upper limit
        upper_limit -= product * factor

        # Append the digit to known digit
        known_digits.append(value)
    return known_digits


def find_all_cases():
    # Initial the digit dictionary
    D = dict()
    for digit in range(0, n):
        D[digit] = digit
    for i in range(9):
        D[digit] = i



print "The millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 is:",
for i in find_smallest_factor():
    print i,
