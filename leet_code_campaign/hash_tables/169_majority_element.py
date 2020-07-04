"""
169. Majority Element

Given an array size of n,

find the majority element.

The majority element is the element that appears
more then [ n / 2 ] times.

You may assume that the array is non empty and
the majority element always does exist in the array

Input: [3,2,3]
Output: 3

Input: [2,2,1,1,1,2,2]
Output: 2


Array

Divide and Conquer Bit Manipulation
Amazon Google Apple Microsoft Yahoo Adobe
""" 

from typing import List
from collections import OrderedDict, Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        host = OrderedDict()
        for n in nums:
            if n in host:
                host[n]+=1
            else:
                host[n] = 1
        
        for k,v in host.items():
            if v > len(nums)//2:
                return k

    def majorityElement_2(self, nums: List[int]) -> int:        
        result = Counter(nums)
        for k,v in result.items():
            if v > len(nums)//2:
                return k



if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement_2([2,2,1,1,1,2,2]))