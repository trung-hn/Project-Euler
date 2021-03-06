# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
known = {0: 0, 1: 1}


def fibonaci(n):
    if n in known:
        return known[n]
    known[n] = fibonaci(n - 1) + fibonaci(n - 2)
    return known[n]


fibonaci(33)  # <4 millions
s = 0
for number in known.values():
    if number % 2 == 0:
        s += number

print ("The sum of Fibonacci numbers that are even and <4 000 000 is:",s)
