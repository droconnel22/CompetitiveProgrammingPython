#!/bin/python3

import math
import os
import random
import re
import sys

"""
Two words are anagram of one another if their letters can be
re-arranged to form the other word.

In this challenge you will be given a string.

YOu must split it into two contigous substrings, then
determine the minimum number of characters to change
to make the two substring into anagrams of one another.

Example:

abccde 

1. break it into two parts
abc
cde

Note that all letters have been used
the substrings are contigous and their lenghts are equal

you can change a and b in the first substring to d and e

to have dec and cde 

which are anagram

Here two changes were necessary


Description

Complete the anagram function in the editor below
It should return the min number of character to change to
make the words anagrams or -1 if its not possible

takes in a string: 

Sample Input

6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx

Sample Output

3
1
-1
2
0
1

Explanation:

Test Case #01: We split s into two strings S1='aaa' and S2='bbb'

we have to replace all three of the characters from the first string
 to make the strings anagrams.

 Test case #2: ab
 you have to replace 'a' with 'b' which will generate 'bb'

 test case #3: abc
 it is not possible for two string of unequal of length to be
 anagrams of one another
 

 test csae #4: mnop
 mn op
 2? 

 test case #5:
 xyyx
xy and yx are already anagrams of one another

Test Case #06 
xaxb bbxx
1 
a-> b


Revisit case 1

aaa

bbb


a:3
b:0

a:0
b:3

"""


# Complete the anagram function below.
def anagram(s):
    if(len(s) % 2 != 0):
        return -1
    a = s[:len(s)//2]
    b = s[len(s)//2:]
    count = 0
    for letter in list(string.ascii_lowercase):
        diff = a.count(letter)-b.count(letter)
        if diff > 0:
            count+=diff
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
