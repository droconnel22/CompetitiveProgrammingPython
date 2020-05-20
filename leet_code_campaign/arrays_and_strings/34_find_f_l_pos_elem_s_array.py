"""

34. Find first and Last Postion of Elment in Sorted Array

Given an array of integers nums sorted in ascending order

find the starting and ending position of a given target  value

Your algorithms runtime complexity must be in the order of O(Log N)

if the target is not found int he array, return [-1,-1]

Example 1:
    Input: nums = [5,7,7,8,8,10] target = 8
    Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Facebook Google Uber Apple LinkedIn Amazon Oracle ByteDance
Neflix Quip(Salesforce)

Array is sorted think biinary search
then first and last position

"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        low_m = -1
        high_m = -1

        while low <= high:
            midpoint = (high-low)//2 + low
            if nums[midpoint] == target:
                low_m = midpoint
                high_m = midpoint
                while low_m > 0 and nums[low_m-1] == target:
                    low_m-=1
                
                while high_m < len(nums)-1 and nums[high_m+1] == target:
                    high_m+=1
                break
            elif nums[midpoint] < target:
                low = midpoint+1
            else:
                high = midpoint-1
        
        return [low_m,high_m]

if __name__ == "__main__":
    s = Solution()
    r = s.searchRange([5,7,7,8,8,10],6)
    print(r)
