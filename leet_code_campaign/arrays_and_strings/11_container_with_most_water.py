"""
11. Container with most water:

Given n non-negative integers, a1, a2, ... , an, where each 
represents a point at coordiante (i,ai)

n vertical lines are drawn such that the two endpoints of a line i is at (i,ai) and (i,0)


Find two lines which together with x-axis forms a container
sucht hat the container contains the MOST water

Note you may not slant the container and n is at least 2.

Example  
arr = [1,8,6,2,5,4,8,3,7]
       1 2 3 4 5 6 7 8 9

    [1,{8},6,2,5,4,8,3,{7}]
     1  *  3 4 5 6 7 8  *

    x_high - x_low = 7
    min(arr[x_high],x_low) = 7
    7 * 7 = 49

Output: 49

Hints:
Array, Two pointers

Find the two largest numbers

"""


from typing import List
import sys

# O(1)
# S(log n)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        x_low = 0
        x_high = len(height)-1
        current_max = -1
        return self.maxAreaHelper(height,x_low,x_high,current_max)
    
    def maxAreaHelper(self,height,x_low,x_high,current_max):
        if x_low > x_high:
            return current_max
        
        current_area = abs(x_high-x_low) * min(height[x_high],height[x_low])
        print(current_area,current_max)
        if current_area > current_max:
            current_max = current_area
        
        # increment
        if height[x_low] < height[x_high]:
            return self.maxAreaHelper(height,x_low+1, x_high, current_max)
        else:
            return self.maxAreaHelper(height,x_low, x_high-1,current_max)



if __name__ == "__main__":
    s = Solution()
    heights= [1,8,6,2,5,4,8,3,7]
    r = s.maxArea(heights)
    print(r)