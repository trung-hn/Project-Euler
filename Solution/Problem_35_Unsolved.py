# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?


from Premade2 import check_prime
import time

known_primes = [2, 3, 5, 7]
know_circular = dict()

# Get all primes number
def get_primes_below(n):
    for i in range(11, n, 2):
        if check_prime(i):
            known_primes.append(i)

# Check if a number is circular prime
def check_circular_primes():
    for num in known_primes:
        list_of_digits = list(str(num))
        list_of_digits.sort()
        string_list = ''.join(list_of_digits)
        if string_list not in know_circular.keys():
            know_circular[string_list] = 1
        else:
            know_circular[string_list] += 1

start_time = time.process_time()
get_primes_below(1000000)
check_circular_primes()

# NOTES: Have not considered the case when the number repeat its self like 11 or 77. 
sum = 0
for i in know_circular.keys():
    if know_circular[i] > 1 :
        sum += know_circular[i]
print(sum)  # 5 comes from 2,3,5,7

# print(know_circular)
print("Time taken: %f" % (time.process_time()-start_time))
