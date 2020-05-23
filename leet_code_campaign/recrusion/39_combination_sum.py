"""
39. Combination Sum

Given a set of candidate numbers (candidates)
(without duplicates) and a target number (target)
find all unique combinations in candidate where the
candidate numbers sums to target

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

Facebook Amazon Microsoft Airbnb Uber

"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def combinationSumHelper(candidates,target,current_index,buffer,global_set):
            # ran out of index
            if current_index == len(candidates):
                return global_set
            
            # Overshot target no need to go further
            if target < 0:
                return global_set

            # good news reached target
            if target == 0:
                #print(buffer)
                global_set.append(buffer)
                return global_set
            
            # two options apply current or move to next
           
            # apply current
        next_buffer = buffer.copy()\
            next_buffer.append(candidates[current_index])

            gs_left = combinationSumHelper(candidates,
            target-candidates[current_index],
            current_index,
            next_buffer,
            global_set)

            # do not apply
            gs_right = combinationSumHelper(candidates,
            target,
            current_index+1,
            buffer,
            global_set)
          
            for item in gs_left:
                if item not in gs_right:
                    gs_right.append(item)
            return gs_right
        
        return combinationSumHelper(candidates,target,0,[],[])

            
if __name__ == "__main__":
    s = Solution()
    r = s.combinationSum([2,3,6,7],7)
    print(r)



            


    