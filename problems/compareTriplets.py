import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    ascore = 0
    bscore = 0
    index = 0
    for num in a:
        if num > b[index]:
            ascore += 1
            index += 1
        elif num < b[index]:
            bscore += 1
            index += 1
        else:
            index += 1

    return [ascore, bscore]



def compareTriplets(a, b):
    # Write your code here
    ascore = 0
    bscore = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            ascore += 1
        elif a[i] < b[i]:
            bscore += 1

    return [ascore, bscore]
