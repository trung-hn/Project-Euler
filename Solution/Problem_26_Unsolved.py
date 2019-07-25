
def check_repeat_fraction(n):
    max_fraction=50
    for i in range(1,max_fraction):
        if (n*(10.0**i-1)).is_integer():
            return i
        if (n*10.0**i).is_integer():
            return 0
    return 0

for i in range(1,1000):
    if check_repeat_fraction(1.0/i)>17:
        print("Number: %d which has the reciprocal of %.15f has %d digit recurring" %(i, 100000.0/i, check_repeat_fraction(1.0/i)))