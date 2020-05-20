"""

217. Contains Duplicate

Given an array of integers, find if the array conttains any duplicates

your functiton should return true if any value appears in the array

at least twice and it should retturn false is very element is 
distinct

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

"""
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for elem in sorted(nums):
            if elem in s:
                return True
            else:
                s.add(elem)
        return False
        