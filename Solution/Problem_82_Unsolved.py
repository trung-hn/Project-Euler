
#ANSWER:
#PROBLEM: Need to update values in the same column differently because they depends on each other.
import PremadeTimer
import numpy as np
from os.path import abspath,dirname

# get data from file
parent_dir=dirname(dirname(abspath(__file__)))
with open(parent_dir+"\data\Problem 82\p082_matrix.txt", "r") as fin:
    line_lst = [line.strip("\n").split(",") for line in fin.readlines()]
    A=np.array(line_lst,dtype=float)# float is very important
print(A)
A=np.array([[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]])


@PremadeTimer.time_this
def calculation(*args):
    max_row=np.size(A,0)
    max_col=np.size(A,1)
    for row in range(max_row-1,-1,-1):
        for col in range(max_col-1,-1,-1):
#             if col==max_col-1:
#                 if row==0: A[row,col]+=A[row+1,col]
#                 if row>0 and row<max_row-1: A[row,col]+=min(A[row+1,col],A[row-1,col])
#                 if row==max_row-1: A[row,col]+=A[row-1,col]
            if col>0 and col<max_col-1:
                if row==0: A[row,col]+=min(A[row+1,col],A[row,col+1])
                if row>0 and row<max_row-1: A[row,col]+=min(A[row+1,col],A[row-1,col],A[row,col+1])
                if row==max_row-1: A[row,col]+=min(A[row-1,col],A[row,col+1])
            if col==0:
                if row==0: A[row,col]+=A[row,col+1]
                if row>0 and row<max_row-1: A[row,col]+=min(A[row+1,col],A[row-1,col],A[row,col+1])
                if row==max_row-1: A[row,col]+=A[row,col+1]
    print(A)
    return np.min(A[:,0])
#
print(calculation())
