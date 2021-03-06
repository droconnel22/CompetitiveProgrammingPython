"""
67. Add Binary

Given two binary strings, return their sum (also a binary string)

The input strings are both non-empty and only contains chars 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

Easy

Facebook Amazon Apple Google

"""


class Solution:
    def addBinary(self, s1: str, s2: str) -> str:
        if not s1 or not s2:
            return ''

        maxlen = max(len(s1), len(s2))

        s1 = s1.zfill(maxlen)
        s2 = s2.zfill(maxlen)

        result  = ''
        carry   = 0

        i = maxlen - 1
        while(i >= 0):
            s = int(s1[i]) + int(s2[i])
            if s == 2: #1+1
                if carry == 0:
                    carry = 1
                    result = "%s%s" % (result, '0')
                else:
                    result = "%s%s" % (result, '1')
            elif s == 1: # 1+0
                if carry == 1:
                    result = "%s%s" % (result, '0')
                else:
                    result = "%s%s" % (result, '1')
            else: # 0+0
                if carry == 1:
                    result = "%s%s" % (result, '1')
                    carry = 0   
                else:
                    result = "%s%s" % (result, '0') 

            i = i - 1

        if carry>0:
            result = "%s%s" % (result, '1')
        return result[::-1]

    def _convert(self, input:str) -> str:
        return ''.join(format(i, 'b') for i in bytearray(input, encoding ='utf-8'))

if __name__ == "__main__":
     s = Solution()
     a = "1010"
     b = "1011"
     r = s.addBinary(a,b)
     print(r)