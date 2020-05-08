"""
1358. Number Of Substrinig Contains All Three Characters

Given a string s consisting only of characters a, b, and c.

Return the number of substrings containing at least one

occurrence of all these characters a,b, and c

Example 1:
Input: s = "abcabc"
Output: 10

Super genius solution:
I appreciate your solution.
After I saw the algorithm, I write a similar code with a comment:

If we know the maximum indices of 'a', 'b' and 'c' in a substring s[0:n] (3 <= n <= len(s)), we will get all the (sub)substrings that share the same right end.

e.g.
substring: aaabc

the maximum index of 'a' is 2
max. index of 'b' is 3
max. index of 'c' is 4

If we take the minimum (that is 2), we get all the 2 + 1 == 3 (sub)substrings s[0:5], s[1:5] and s[2:5].

Then we can pick up all the (sub)substrings for all substrings of each length (s[0:3], s[0:4], s[0:5]... s[0:]).

"""

from typing import List,Set
import re

class Solution:
    def novel(self,s:str) -> int:
        maxA = maxB = maxC = ans = 0
        for i in range(len(s)):
            if s[i] == 'a':
                maxA = i + 1
            elif s[i] == 'b':
                maxB = i + 1
            else:
                maxC = i + 1
            
            ans += min(maxA,maxB,maxC)
        return ans

    def numberOfSubstrings(self, s: str) -> int:
       result_set = self.helper(s,0)
       count = 0
       #print(sorted(result_set))
       for word in result_set:
           if self.contains("abc",word):
               print("valid:",word)
               count+=1
       return count

    
    def helper(self,seqeuence:str, index:int) -> Set[str]:
        permutations = None
        if index == len(seqeuence):
            permutations = set()
            permutations.add("")
            return permutations
        else:
            local_permutations = set()
            permutations = self.helper(seqeuence,index+1)
            for permutation in permutations:
                letter = seqeuence[index]
                next_permutation =permutation+letter
                sorted_next_perm = "".join(sorted(next_permutation))
                local_permutations.add(sorted_next_perm)
            permutations.update(local_permutations)
            return permutations
    
    def contains(self,substring, word):     
       truth_dict = {}
       for required_letter in substring:
           truth_dict[required_letter] = False
       for letter in word:
           if letter not in substring:
               return False
           if letter in truth_dict:
                truth_dict[letter] = True
       for key,value in truth_dict.items():
            if value is False:
                return False
       return True




if __name__ == "__main__":
   s = Solution()
   scenarios = ["abcabc","aaacb","abc"]
   for scen in scenarios:
       print(s.numberOfSubstrings(scen))
