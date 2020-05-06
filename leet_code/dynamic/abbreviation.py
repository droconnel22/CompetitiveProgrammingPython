#!/bin/python3

import math
import os
import random
import re
import sys


"""
You can perform the following operations on the string, a:
1. Capitalize zero or more of a's lowercase letters
2. Delete all of the remaining lowercase letters in a

Given two strings, a and b, determine if it's possible to make a
equal to b as describeed. If so print YES on a new line,
otherwise print NO.

Example
a = AbcDE 
b - ABDE

in a we can convert b a
delete c to match b
if a = AbcDE
and b = AFDE
matching is not possible because letters may only be capitalized or discarded
not changed

Function Description
Complete the function abbreviation in the editor below.
It must return either YES or NO.

a: The string to modify
b: The string to match

Input Format
the first line contains a single integer q, the number of queries

only [A-Z]

Examples

Input
1
daBcd
ABC

daBcd -> dABCd -> ABC
1. Capitalize the letter a and c in A so that a = dABCd
2. delete all the reamining lowercase letters in a so that a = ABC

Actions
1. Capitalize zero or more of a's lowercase letters
2. Delete all of the remaining lowercase letters in a

Output
YES


Example 2:


A: daBcd 
B: ABC

Ask questions!!
- ok so I can only perform two operations
1. captilaze none or all of a's lowercase letters
2. delete all of the remaing lowercase letters in a

- what if I sorted both?
find first letter in a that matches 
so for each letter in a what do I need to know
is its counterpart in B
is it in the right position
is it not in b
can i delete it 

Example 3:

a:AbCdE
b: AFE

does a[0] exist in b as a capital?
-yes -> captialize X
-no -> delete

does a[1] exit in b as a capital?
- yes -> captialize 
- no -> delete X

a:ACDE
b:AFE

does a[2] exist in b as a captial
- no -> delete, keep index in place

a:ADE
b:AFE


optimization ? - check a for all letters in b either capital or not
if they don't exist you'll know it cant be

Example 4:
beFgH
EFG

Example 5:

beFgH
EFH


a:
:XMQKLR
no

TZXTQMQcKGLR
BTZXMQKLR

"""

# Complete the abbreviation function below.
def abbreviation(a, b):
    m, n = len(a), len(b)
    dp = [[False]*(m+1) for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n+1):
        for j in range(m+1):
            if i == 0 and j != 0:
                dp[i][j] = a[j-1].islower() and dp[i][j-1]
            elif i != 0 and j != 0:
                if a[j-1] == b[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif a[j-1].upper() == b[i-1]:
                    dp[i][j] = dp[i-1][j-1] or dp[i][j-1]
                elif not (a[j-1].isupper() and b[i-1].isupper()):
                    dp[i][j] = dp[i][j-1]
    return "YES" if dp[n][m] else "NO"

def abbreviation2(a,b):
    m,n = len(a), len(b)
    dp = [[False]*(m+1) for _ in range(n+1)]
    dp[0][0] = True
    for i in range(n+1):
        for j in range(m+1):
            # top row
            if i == 0 and j != 0:
                # if a is lower case and dp is capita or false or??
                dp[i][j] = a[j-1].islower() and dp[i][j-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
