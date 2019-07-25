# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

# *From experience, after every 239.1 n, the number of digits increase by 50
# *Fib(n):           716    955    1195    1434    1673    1912    2152    2391    4782
# *Number of digits: 150    200    250     300     350     400     450     500     1000

# *Should consider to try Binet's Formula
# *http://artofproblemsolving.com/wiki/index.php/Binet%27s_Formula


import Premade

i = 2391
fibo_list = Premade.fibonacci(i)
for num in fibo_list:
    number = fibo_list[num]
    if number > 10 ** 1000 or num == i - 1:
        print ("Index:", num)
        print (number)
        print ("Number of digits:", len(str(number)))
        break

len_list = list()
for num in fibo_list:
    number = fibo_list[num]
    len_list.append(len(str(number)))
    # print len(str(number)),
histogram = {}
for leng in len_list:
    histogram[leng] = histogram.get(leng, 0) + 1
# print "\n", histogram.values()
count = 0
totalcount = 0
for his in histogram.values():
    if his == 4:
        print (count,end="")
        count = 0
    if his == 5:
        count += 1
    totalcount += 1
    # print "\n",totalcount
    # print fibo_list
