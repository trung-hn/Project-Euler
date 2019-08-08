
# ANSWER:427337
# NOTES: remember to have array as dtype=float or else value won't change when re-assign

import PremadeTimer
import numpy as np
from os.path import abspath, dirname

# get data from file
parent_dir = dirname(dirname(abspath(__file__)))
with open(parent_dir+"\data\Problem 81\p081_matrix.txt", "r") as fin:
    line_lst = [line.strip("\n").split(",") for line in fin.readlines()]
    A = np.array(line_lst, dtype=float)  # float is very important

print("Read in array:\n", A)


@PremadeTimer.time_this  # Timer
def calculation(*args):
    max_row = np.size(A, 0)
    max_col = np.size(A, 1)
    for row in range(max_row):
        for col in range(max_col):
            if col == 0 and row == 0:
                continue
            if col == 0 and row > 0:
                A[row, col] += A[row-1, col]
            if row == 0 and col > 0:
                A[row, col] += A[row, col-1]
            if row > 0 and col > 0:
                A[row, col] += min(A[row-1, col], A[row, col-1])
    print("Analyzed array:\n", A)
    return A[np.size(A, 0)-1, np.size(A, 1)-1]


print(calculation())
