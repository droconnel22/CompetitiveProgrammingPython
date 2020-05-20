"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring
without repeating characters

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         if s == " ":
            return 1
        if len(s) <= 1:
            return len(s)
        
        max_count = 0
        for index in range(len(s)-1):
            buffer = s[index]
            next_index = index+1
            while next_index < len(s) and s[next_index] not in buffer:
                buffer+=s[next_index]
                next_index+=1
            
            if len(buffer) > max_count:
                max_count = len(buffer)
        
        return max_count


if __name__ == "__main__":
    s = Solution()
    r = s.lengthOfLongestSubstring("bbbbbbb")
    print(r)