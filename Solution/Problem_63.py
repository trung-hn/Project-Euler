# The 5-digit number, 16807=7(5), is also a fifth power. Similarly, the 9-digit number, 134217728=8(9), is a ninth power.
# How many n-digit positive integers exist which are also an nth power?

# ANSWER: 48
number_set=set()
def calculation(n):
    for a in range(1,n+1):
        for b in range(1,n+1):
             temp=a**b
             if b== len(str(temp)):
                 number_set.add(temp)
                 print("%d**%d="%(a,b),temp)

calculation(20)

print("--------------------------------------------\n\
Total number of integers satisfying the requirement:",len(number_set))
