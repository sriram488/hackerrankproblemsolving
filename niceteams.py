#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'maxPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY skillLevel
#  2. INTEGER minDiff
#

def maxPairs(skillLevel, minDiff):
    skillLevel.sort()
    n = len(skillLevel)
    i = 0
    pairs= []
    for j in range(n // 2):
        while i < n and skillLevel[i] - skillLevel[j] < minDiff:
            i += 1
        if i >= n:
            break
        pairs.append(i)
    pairs = pairs[:(n // 2)]
    result = 0
    k = n - 1
    for y in reversed(pairs):
        if y <= k:
            result += 1
            k -= 1
    return result

n=6
skillLevel = [3,4,5,2,1,1]
print(maxPairs(skillLevel, 3))
