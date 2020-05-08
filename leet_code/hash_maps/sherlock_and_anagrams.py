import math
import os
import random
import re
import sys
"""
Sherlock and Anagrams

Two string are anagrams of each other if the letters of one string
can be rearranged to form the other string.

Given a string, find the number of pairs of substrings of the string
that are anagrams of each other.

Anagram:
An anagram is a permutation onlly applicable to strings
It's a re-arrangement of the characters.

Two strings are called an anagrammatic pair when they
have the same length and and the same set of characters.

for example

s = mom
[m,m],[mo,om],[]


Example
2

abba
abcd

[a,a]
[ab,ba]
[abb,bba]

#Two strings are anagrams of each other if the
#  letters of one string can be rearranged to 
# form the other string. 
# 
# Given a string, find the number of pairs 
# of substrings of the string 
# that are anagrams of each other.
#  pairs of substrings
# for mother note order is preserved




[a]
[ab]
[cd]

1
cdcd

c:2
d:2


Example 
1
ifailuhkqq


how would i find this?
Split all letters and count 2's or 4's

i,i
q,q
ifa,fai

i:2
f:1
a:1
l:1
u:1
h:1
k:1
q:2

Two strings are anagrams of each other 
if the letters of one string can be 
rearranged to form the other string.

#that represents the number of anagrammatic pairs

"""


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    return helper(s,1)

def helper(sequence,index):
    if sequence is None:
        return None
    
    permutations = None
    if(index == len(sequence)):
        permutations = []
        return permutations
    else:
        local_permutations = []
        a = sequence[:index]
        b = sequence[index:]
        print(a,b)
        permutations = helper(sequence, index+1)
        for perm in permutations:
            temp = perm+a
            print(perm+a)
            print(perm+b)
            local_permutations.append(temp)
        permutations.extend(local_permutations)
    return permutations


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()