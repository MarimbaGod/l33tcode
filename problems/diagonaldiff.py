#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left = 0
    right = 0
    for index in range(len(arr)):
        left += arr[index][index]

    for index in range(len(arr)):
        right += arr[index][(len(arr)-1) - index]
        #BUT WHYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY

    return abs(left-right)


# def diagonalDifference(arr):
    # n = len(arr)
    # left_sum = 0
    # right_sum = 0

    # for i in range(n):
    #     left_sum += arr[i][i]
    #     right_sum += arr[i][n-i-1]
    ##### essentailly the same, just setting the
    # variable n = len(arr)

    # return abs(left_sum - right_sum)
