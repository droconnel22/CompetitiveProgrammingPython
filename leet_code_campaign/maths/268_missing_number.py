"""

268. Missing Number

Given an array containing n distinct numbers taken from 
0,1,2,..., n find the one that is missing from the array.

Example 1:
Input [3,0,1]
Output: 2

Example 2:
Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Noote:
Your algorithm should run in linear runtime comoplexity.

Could you implement it using oonly constant extra space
complexity

Amazon | Microsoft | Apple

Array, Math, Bit Manipulation

hash maps loop over the array set the current lement as true in
the map

use a mirrored hashmap (more space)
O(N)

"""

from typing import List



class Solution:
    # O(N)
    # S(1)
    # Gauss Formula
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = 0
        n = len(nums)
        while n >= 0:
            expected_sum +=n
            n-=1
        return expected_sum - sum(nums)

if __name__ == "__main__":
    s = Solution()