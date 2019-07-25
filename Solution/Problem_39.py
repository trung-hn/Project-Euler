# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?
# ANSWER: 840

import math

# Make a dictionary containing the histogram of each p
histogram=dict()
for p in range(2,1000):
    for a in range(1,p-1):
        b=(2.0*a*p-p**2)/(2*(a-p))
        if b.is_integer() and b>0:
            c=math.sqrt(a**2.0+b**2)
            if c.is_integer():
                if p in histogram.keys():
                    histogram[p] +=1
                else:
                    histogram[p]=1

# Print highest value in dictionary.
highest=0
for key in histogram.keys():
    if histogram[key]>highest:
        highest=histogram[key]
        result=key

print(result)