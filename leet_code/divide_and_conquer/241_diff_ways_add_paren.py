import re
"""

241. Different Ways to Add Parentheses

Given a string of number and operators 
return all possible results
from computnig all the different possible
ways to group numbers and operators

The valid operators are +,- and *.

Example 1:

Input: "2-1-1"
Output: [0,2]

Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Example 2:
Input: "2*3-4*5"
Output: [-34, -14, -10, -10 ,10]

Explanation:
(2*(3-(4*5))) = -34
(2*((3-4)*5)) = -10

((2*3)-(4*5)) = -14

((2*(3-4))*5) = -10

(((2*3)-4)*5)


"""



class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        index = 0
        # searched is str:int
        searched = {}
        permutations = []
        for i in range(len(input)):
            prefix = input[i:i+3]
            if(re.match("\d*\W\d*",prefix)):
                compute_result = self.compute(prefix)
                if compute_result:
                    permutations.append(prefix)
        print(permutations)
     
    def compute(self, sequence):        
        numbers = re.findall(r'\d+',sequence)
        print(numbers)
        if numbers is None:
            return None
        if "*" in sequence:
            result = 1
            for num in numbers:
                result+=int(num)
        elif "+" in sequence:
            return sum(numbers)
        elif "-" in sequence:
            result = int(numbers[0])
            for num in range(1,len(numbers)):
                result -=int(num)
            return result

if __name__ == "__main__":
    input = "2*3-4*5"
    input2 = "2-1-1"
    s = Solution()
    r= s.diffWaysToCompute(input)
    print(r)