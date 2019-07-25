# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below:


# NOTES: Approach: take A[2][1]=47 for example, take this and combine with the maximum of 2 values above it. Do it for all value => 47 + (95 +75)
# ANSWER: 1074
import numpy as np
string = "\
75 \
95 64 \
17 47 82 \
18 35 87 10 \
20 04 82 47 65 \
19 01 23 75 03 34 \
88 02 77 73 07 63 67 \
99 65 04 28 06 16 70 92 \
41 41 26 56 83 40 80 70 33 \
41 48 72 33 47 32 37 16 94 29 \
53 71 44 65 25 43 91 52 97 51 14 \
70 11 33 28 77 73 17 78 39 68 17 57 \
91 71 52 38 17 14 91 43 58 50 27 29 48 \
63 66 04 68 89 53 67 30 73 16 69 87 40 31 \
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"

list_number = string.split(" ")
# Convert string to int
list_number = [int(i) for i in list_number]
A = np.zeros((15, 15), dtype=np.int32)

# Convert list to 2D Array
k = 0
for i in range(0, 15):
    for j in range(0, i+1):
        A[i][j] = list_number[k]
        k += 1

# Sum up rows
for i in range(1, 15):
    # First column
    A[i][0] += A[i-1][0]
    # Middle columns
    for j in range(1, i):
        A[i][j] = A[i][j] + max(A[i-1][j-1], A[i-1][j])
    # Last column
    A[i][i] += A[i-1][i-1]

print("Maximum total at last row:", max(A[14]))