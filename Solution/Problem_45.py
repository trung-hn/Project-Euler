# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
# Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
# Pentagonal 	  	Pn=n(3n−1)/2 	  	1, 5, 12, 22, 35, ...
# Hexagonal 	  	Hn=n(2n−1) 	  	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
# Find the next triangle number that is also pentagonal and hexagonal.

# ANSWER: 1533776805

import math

triangle_number=list()

# Generate a list of triangle number
for i in range(1,300000):
    triangle_number.append(i*(i+1.0)/2)

for i in triangle_number:
    # Root of polynomial for pentagonal and hexagonal
    pentagonal_root=(math.sqrt(1+24*i)+1)/6
    hexagonal_root=(math.sqrt(1+8*i)+1)/4
    if pentagonal_root.is_integer() and hexagonal_root.is_integer():
        print("The triangle number is: %d" %(i))