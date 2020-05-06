"""
Sherlock and the Valid String

Sherlock considers a string totbe valid if 
all the characters of the string appear
the same number of times.

it is also valid if he can remove just 1
character at 1 index in the string 
and the remaining characters will
occur the same number of times.

Given a string s, determine if it is valid
if so return YES, otherwise return NO.

For example if s = abc
it is a valid string because frequences are
a:1
b:1
c:1

so is
s = abcc because we can remove one c and have 1
of each charactter in the remainiing strings

if s = abccc
it is is not valid as we can
only remove 1 ocurrence of c,
that would leave the character frequences 

Constraints
1 < s < 10 ^5

ALL CHARACTERS APPEAR THE SAME NUMBER OF TIMES.
YOU WON'T KNOW FOR SURE UNTIL THE END.

# SORT THROUGH
# CREATE HASH MAP BASED ON ALPHA BET
# CHECK IF MORE THEN 3 UNIQUE VALUES.
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import string
from collections import Counter


# Complete the isValid function below.
def isValid100(s):
    # frequencies of all letters
    freq = Counter(s)
    # frequencies values sorted
    values = sorted(freq.values())
    # max frequencie value
    v_max = max(values)
    # min frequencie value
    v_min = min(values)
    # max frequencie value repetitions
    max_count = values.count(v_max)
    # min frequencie value repetitions
    min_count = values.count(v_min)
    # frequencie of frequencie values, made some validations more easy 
    freq_values = Counter(values)

    # more then 2 frequencies repeat, this case string can be valid, case: aaabbc
    if len(freq_values) > 2:
        return 'NO'
    # only 1 frequencie repeat, so, is a valid string, case: aabbcc
    elif len(freq_values) == 1:
        return 'YES'
    # min frequencie count is 1, so, just remove one value to turn the string valid, case: aab
    elif min_count == 1:
        return 'YES'
    # max frequencie minus your repeatitions equal min value, case: bbaaa, just remove
    # one of the same letter repeatitions to turn the strig valid
    elif v_max - max_count == v_min:
        return 'YES'
    # other cases are not valids
    else:
        return 'NO'

# 
def isValid(s):
    def isValid(s):
    if len(s) <= 3:
        return "YES"
    sorted_s = sorted(s)
    expected_level = -1
    expected_level_2 = -1
    current_level = 0
    current_letter = None
    for letter in sorted_s:
        if current_letter is None:
            current_letter = letter
        print(current_letter,letter, current_level,expected_level,expected_level_2)
        if current_letter == letter:
            current_level+=1
        else:            
            # first letter sets the expectations
            if expected_level == -1:
                expected_level = current_level
            elif expected_level_2 == -1 and abs(current_level-expected_level) == 1:
                expected_level_2 = current_level
            elif current_level != expected_level and current_level != expected_level_2:
                    return "NO"                       
            current_letter = letter
            current_level = 1
    #print(current_letter,letter, current_level,expected_level,expected_level_2)
    if current_level != expected_level and expected_level_2 == -1:
        return "YES"
    elif current_level != expected_level_2 and expected_level == -1:
        return "YES"
    elif current_level != expected_level and current_level != expected_level_2:
        return "NO"   
    else:
        return "YES"


if __name__ == '__main__':
    print(isValid("abcdefghhgfedecba"))
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #s = input()

    #result = isValid(s)

    #fptr.write(result + '\n')

    #fptr.close()