# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
# ANSWER: 21124
known_number = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7,
                17: 9, 18: 8, 19: 8, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6, 1000: 11}

def count_words_upto(n):
    for number in range(21, n + 1):
        firstD = int(number/100)
        secondD = int(number/10)-firstD*10
        thirdD = number-firstD*100-secondD*10
        
        # Calculate no of letters for the number
        if secondD != 1:
            letter = known_number[firstD] + \
                known_number[secondD*10]+known_number[thirdD]
        else:
            letter = known_number[firstD]+known_number[number-firstD*100]
        
        # Hundred number
        if firstD:
            letter += 10  # Because of the word "hundred and"
        if (secondD == 0 and thirdD == 0):
            letter -= 3  # Get rid of the word"and"
        known_number[number] = letter


count_words_upto(999)
# print(known_number)
print(sum(known_number.values()))
