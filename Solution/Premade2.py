import math
# Check if a number a prime or not

def check_prime(n):

    # # Divisibility by 2 or 5
    if n%10 in {0, 2, 4, 5, 6, 8}:
        return False
    # Divisibility by 3
    sum = 0
    for digit in str(n):
        sum += int(digit)
    if sum % 3 == 0:
        return False

    # Divisibility by or 5
    # if n % 5 == 0:
    #     return False

    # Divisibility by any number
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
