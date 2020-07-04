"""
136 Single Number

Given a non-empty array of integers,
every element appears twice except for one
Find that single one.

Note:

Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?

Facebook, Bloomberg Amazon Apple Microsoft

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4

Options
map with values select the one that 1

"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        memo = {}
        for num in nums:
            if num in memo:
                memo[num]+=1
            else:
                memo[num] = 1
        for k,v in memo.items():
            if v == 1:
                return k
        return -1
    
    def singleNumber_no_extra(self, nums: List[int]) -> int:
        """
        Approach 4: Bit Manipulation
        Concept
        If we take XOR of zero and some bit, it will return that bit
        a \oplus 0 = aa⊕0=a
        If we take XOR of two same bits, it will return 0
        a \oplus a = 0a⊕a=0
        So we can XOR all bits together to find the unique number.

        """
        a = 0
        for i in nums:
            a ^= i
        return a

if __name__ == "__main__":
    s = Solution()
    s.singleNumber([4,1,2,1,2])
