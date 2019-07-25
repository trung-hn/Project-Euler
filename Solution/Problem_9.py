# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import time

t0 = time.time()
maxi = 999
found = 0
for a in range(1, maxi / 2):
    for b in range(a, maxi / 2):
        for c in range(b, maxi):
            if c > a + b:
                break
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                found = 1
                print (a, b, c, "are the numbers that have sum=1000 and a^2+b^2=c^2 and a<b<c")
                print ("Product of these numbers is:",a * b * c)
                break
        if found:
            break
    if found:
        break
print (time.time() - t0)
