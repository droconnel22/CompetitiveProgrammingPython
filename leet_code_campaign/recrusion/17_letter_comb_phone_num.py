"""
17. Letter Combinations of a phone number

Given a string containing digits from 
2-9 inclusive, return all possible letter
combinations that the number could
represent.

A mapping of digit to letters (just like the 
telephone buttons is given below.)
Note that 1 does not map to any letters.
1 -> inf
[
2 -> abc
3 -> def
4 -> ghi
5 -> jkl
6 -> mno
7 -> pqrs
8 -> tuv
9 -> wxyz
]

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:

Although the above answer is in lexicographical order, 
your answer could be in any order you want.

Amazon Microsoft Google Atlassian
Oracle Walmart Labs Lyft Square
Uber Apple Salesforce Nutanix
"""
from typing import List
class Solution:
    

    def letterCombinations(self, digits: str) -> List[str]:
        # Create string from digits
        dialpad = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
       
        word_list = []
        for num in list(map(int,digits)):
            if num in dialpad:      
                word_list.append(dialpad[num]) 
        alpha_index = 0
        letter_index = 0     
        result = set()

        def helper(word_list,alpha_index,letter_index,sub_string,result):  
            if len(sub_string) == len(word_list):
                result.add(sub_string) 
            if alpha_index == len(word_list):                       
                return
            if letter_index == len(word_list[alpha_index]):
                return
            next_word = sub_string+word_list[alpha_index][letter_index]
            helper(word_list,alpha_index+1,letter_index, next_word,result)
            helper(word_list,alpha_index,letter_index+1,sub_string,result)
            helper(word_list,alpha_index,letter_index+1,next_word,result)

        helper(word_list,alpha_index,letter_index,"",result)
        return list(result) 

    
        


if __name__ == "__main__":
    s = Solution()
    input = "268"
    r = s.letterCombinations(input)
    print(r)
    
