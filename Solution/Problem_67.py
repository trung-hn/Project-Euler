# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below:


# NOTES: See Problem 18 for simpler example
# Approach: take A[2][1]=47 for example, take this and combine with the maximum of 2 values above it. Do it for all value => 47 + (95 +75)
# ANSWER:

import numpy as np
Size = 100
A = np.zeros((Size, Size), dtype=np.int32)

fin = open(
    "D:\OneDrive\Study\Self learning\Coding\Project Euler\data\Problem 67\p067_triangle.txt", "r")
number_list = fin.readlines()
fin.close()

# Remove \n on each line in the text file
number_list = [i.rstrip('\n') for i in number_list]

# Put each number in each line as a element in a list
list_of_number = list()
for row_of_number in number_list:
    for number in row_of_number.split(' '):
        list_of_number.append(number)

# Convert string to int
list_of_number = [int(i) for i in list_of_number]



# Convert list to 2D Array
k = 0
for i in range(0, Size):
    for j in range(0, i+1):
        A[i][j] = list_of_number[k]
        k += 1
# Sum up rows
for i in range(1, Size):
    # First column
    A[i][0] = A[i][0]+A[i-1][0]
    # Middle columns
    for j in range(1, i):
        A[i][j] = A[i][j] + max(A[i-1][j-1], A[i-1][j])
    # Last column
    A[i][i] = A[i][i]+A[i-1][i-1]

print("Maximum total at last row:", max(A[Size-1]))
