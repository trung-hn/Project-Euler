# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009
# Find the largest palindrome made from the product of two 3-digit numbers.
# Answer: 906609

number_list=list()
for x in range(100, 999):
    for y in range(x, 999):
        result = x * y
        result_str = str(result)
        if len(result_str)==5:
            if result_str[0:2] == result_str[-1:2:-1]:
                number_list.append(result)
        if len(result_str)==6:
            if result_str[0:3]== result_str[-1:2:-1]:
                number_list.append(result)
print ("The largest palindrome made from the product of two 3-digit numbers is:",max(number_list))
