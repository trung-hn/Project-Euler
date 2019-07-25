# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
#3025 minus 385 is 2640

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_square=0
square_of_sum=0

for i in range(1,101):
    sum_of_square+= i ** 2
    square_of_sum+=i
square_of_sum= square_of_sum ** 2

print "The difference between sum of squares and square of sum is:", square_of_sum - sum_of_square
