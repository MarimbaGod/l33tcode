# Given an array of integers, calculate the ratios of its elements that are positive,
# negative, and zero. Print the decimal value of each fraction on
# a new line with  places after the decimal.

# Note: This challenge introduces precision problems.
# The test cases are scaled to six decimal places, though answers with
# absolute error of up to  are acceptable.

# Ex... arr = [1, 1, 0, -1, -1]

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    total = len(arr)
    for num in arr:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1

    print(pos/total)
    print(neg/total)
    print(zero/total)
