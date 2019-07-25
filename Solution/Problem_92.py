# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

# For example,
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
# How many starting numbers below ten million will arrive at 89?

# ANSWER: 8581146. Time taken: 26s for resursive, 
import time

# Set of numbers which eventually lead to 1 and 89
set_of_number_leads_to_89 = {89}
set_of_number_leads_to_1 = {1}

# Method using recursive (slower)
def chain_stop_at_89_recursive(n):
    """
    Method using recursive (slower)
    """
    next_number = 0
    for digit in str(n):
        next_number += int(digit)**2

    # Return False if number will eventually lead to 1
    # Return True if number will eventually lead to 89
    if next_number in set_of_number_leads_to_1:
        set_of_number_leads_to_1.add(n)
        return False
    elif next_number in set_of_number_leads_to_89:
        set_of_number_leads_to_89.add(n)
        return True
    else:
        # Else, use recursive function (call itself)
        return chain_stop_at_89_recursive(next_number)

# Method don't use recursive (faster)
def chain_stop_at_89_non_recursive(n):
    """
    Method don't use recursive (faster)
    """
    while (1):
        next_number = 0
        for digit in str(n):
            next_number += int(digit)**2

        # Return False if number will eventually lead to 1
        # Return True if number will eventually lead to 89
        if next_number in set_of_number_leads_to_1:
            set_of_number_leads_to_1.add(n)
            return False
        elif next_number in set_of_number_leads_to_89:
            set_of_number_leads_to_89.add(n)
            return True
        n = next_number

initial_time = time.process_time()

count = 0
for i in range(1, 10000000):
    if (chain_stop_at_89_non_recursive(i)):
        count += 1
        # print(count)
print(count)

print("Time taken: %.10f" % (time.process_time()-initial_time))