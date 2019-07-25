# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
#  begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
#  by its alphabetical position in the list to obtain a name score.

# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
# 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

# What is the total of all the name scores in the file?
import time
alphabet = {}
al = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 1

# Creating a alphabet dictionary
for letter in list(al):
    alphabet[letter] = count
    count += 1

# Text file
fo = open("data\Problem 22\p022_names.txt", "r")
for i in fo:
    name_string = i
name_string = name_string.replace('\"', "")  # delete quotation mark
name_list = name_string.split(",")  # split into a list of name
name_list.sort()  # Sort in alphabet order


def calculate_score():
    result = 0
    for name in name_list:
        score = 0
        for letter in list(name):
            score += alphabet[letter]
        result += score * (name_list.index(name) + 1)
    return result

t0=time.clock()
print "The total of the name score if the sorted file is:",calculate_score()
print "Time took:",time.clock()-t0