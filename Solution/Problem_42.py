# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
# ANSWER: 162

import math
import time
# Get Data
fin=open("D:\OneDrive\Study\Self learning\Coding\Project Euler\data\Problem 42\p042_words.txt","r")
string_content=fin.readline()
fin.close()

char_dict={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13, "N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

# Split data into element of a list
string_list=list()
string_list=string_content.replace('"','').split(',')

# Check if it is tran
def is_triangle_number(n):
    # Check if root is integer
    root=(-1+math.sqrt(1+8.0*n))/2
    if root.is_integer():
        return True
    return False    

def calculation():
    count=0
    # For each word in string list
    for word in string_list:
        sum=0
        # For each char in each word
        for char in word:
            sum += char_dict[char]
        if is_triangle_number(sum):
            count +=1
    print(count)
calculation()

