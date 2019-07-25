# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
# Answer: 972


def calculation():
    max = 0
    for a in range(0, 101):
        for b in range(0, 101):
            digit_sum = 0
            for digit in str(a**b):
                digit_sum += int(digit)
            if max < digit_sum:
                max = digit_sum
    return max


print("The maximu digital sum is:", calculation())
