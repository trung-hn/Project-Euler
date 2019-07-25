# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
# ANSWER: 142857

big_dict=dict()
big_list=list()
def calculation(n):
    for i in range(1, n):
        # 6 numbers
        list_of_numbers=[i,i*2,i*3,i*4,i*5,i*6]
        k=0
        for num in list_of_numbers:
            big_list=list()
            # Represent number as array of digits
            for string_digit in str(num):
               big_list.append(int(string_digit))
            # Put array in dictionary
            big_dict[k]=sorted(big_list)
            k+=1 
        # If all 6 numbers have the same digit
        if big_dict[0]==big_dict[1] and big_dict[0] ==big_dict[2] and big_dict[0]==big_dict[3]:
            if big_dict[0]==big_dict[4] and big_dict[0] ==big_dict[5]:
                print("Number that satisfies the rule is: ",i)
                break
calculation(500000)