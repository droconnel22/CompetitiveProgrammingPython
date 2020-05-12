"""
Given an array A of integers
return true if and only if it is a
valid mountain array

recall taht A is a mountain if and noly if

A. length >= 3
There exist some ii with 0 <i < a.length-i such that
- A[0] < A[1] < ... A[i-1] < A[i]
- A[i] > A[i+1] > ... > A[A.length-1]

Valid mountain
[0,2,3,4,5,2,1,0]

Invalid
[0,2,3,3,5,2,1,0]

Example 1:
Input: [2,1]
Output: false

Example 2:
Input: [3,5,5]
Output: false

Example 3:
Input: [0,3,2,1]
Output: true

It's very easy to keep track of a monotonically 
increasing or decreasing ordering of elements. 
You just need to be able to determine the 
start of the valley in the mountain 
and from that point onwards, 
it should be a valley i.e. no mini-hills after that. 

Use this information in regards to the values 
in the array and you will be able to come up 
with a straightforward solution.
"""

from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False

        goingUp = True
        for i in range(len(A)-1):
            print(A[i],end=", ")
            if A[i] == A[i+1]:
                return False
            elif goingUp and A[i] > A[i+1]:
                 goingUp = False
            elif not goingUp and A[i] < A[i+1]:
                return False
        return True

    def validMountainArray_2(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False
        
        low = 0
        high = len(A)-1

        # The crest can not be equal to the low or high
        high_index = 0
        high_num = 0
        for i in range(1,len(A)):
            if A[i-1] == A[i]:
                return False
            elif A[i-1] < A[i]:
                high_index = i
                high_num = A[i]
        
        if high_index == low or high_index == high:
            return False
        return True

    # Space complexity: O(1)
    # Time complexity: O(N)
    def validMountainArray_3(self, A: List[int]) -> bool:
        if len(A) < 3:
            return False        
        low = 0
        high = len(A)-1
        i = low
        while i < len(A)-1 and A[i] < A[i+1]:
            i+=1
        j = high
        while j >= 0 and A[j-1] > A[j]:
            j-=1
        return i == j and i != low and j != high

    def recommended_solution(self, A:List[int]) -> bool:
        i = 1
        while i < len(A) and A[i] > A[i-1]:
            i+=1
        if i ==1 or i == len(A):
            return False
        while i < len(A) and A[i] < A[i-1]:
            i+=1
        return i == len(A)

if __name__ == "__main__":
    s = Solution()
    arr  = [0,1,2,3,4,5,4,3,2,1,2,1,0]
    print(s.validMountainArray_3(arr))