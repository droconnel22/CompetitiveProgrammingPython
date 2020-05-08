"""
Given an array of integers write a function to move all
0's to the end while maintains the relative order
of the other elements

Given an array nums, write a function to move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

the number of zeros at the end of array

count of non zero elements is 3

start from j to to the end of 3 we should see only zeros

Steps:

1. Define a pointer j at the beginning of the array
2. Loop over every element in the array 
3. if the current element is not zero set the element
at j to it and increment j
once we find a non zero element we push it to the front of array
by pushing setting the value at position j
4.  after loop ends set all elements from the position to end of array to zero


A two-pointer approach could be helpful here. 
The idea would be to have one pointer for 
iterating the array and another pointer that just 
works on the non-zero elements of the array.
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Time => O(2*N) = O(N)
        # Space => O(1)
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j+=1
        for i in range(j,len(nums)):
            nums[i] = 0
        
               

if __name__ == "__main__":
    s = Solution()
    arr = [1,0,0,1,0,0,1]
    s.moveZeroes(arr)
    print(arr)
        