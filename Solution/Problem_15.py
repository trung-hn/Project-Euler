# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

# Pascal's Triangle
# 1
# 1   1
# 1   2   1
# 1   3   3   1
# 1   4   6   4   1
# 1   5   10  10  5   1
# 1   6   14  20  14  6   1
# 1   7   21  35  35  21  7   1

# ANSWER: 137846528820

import numpy as np

maxrow = 41
wanted_index = 20
A = np.zeros((maxrow, maxrow), dtype=np.int64)

# Initialize 1 at the beginning and at the end of each row
for i in range(0, maxrow):
    A[i][0] = 1
    A[i][i] = 1

# Fill in the rest
for i in range(2, maxrow):
    for j in range(1, maxrow-1):
        A[i][j] = A[i-1][j-1]+A[i-1][j]

k = 0
# Print Pascal's Triangle to screen
for arr in A:
    if k/2 > 10:
        break
    print("For box size %.1f:" % (k/2), end="")
    k += 1
    for a in arr:
        if a != 0:
            print("%7d" % (a), end="")
    print("\n")


print("The number of ways is: ", A[wanted_index*2][wanted_index])
