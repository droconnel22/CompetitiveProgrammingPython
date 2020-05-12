"""
278 First Bad Version

Binary search

You are a product manager and currently lead a team to 
develop a new product.

Unfortunetly the latest version of your product fails
the quality check.

Since each version is developed based on the previouos
version, all the versiono after a bad version are also bad.

Suppose you have n version [1,2,...,n] and you want to find
out the first bad one, which all causes all the following ones
to be bad

You are given an api bool is badVersion(version)
which will return whether a version is bad.

Implement a function to find the first bad version.

You should minimize the number of calls to the api

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 


"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n-1        
        while low <= high:
            mid = (high-low)//2+low
            mid_result = isBadVersion(mid)
            if mid_result is False:
                low = mid+1
            elif mid_result is True:
                high = mid-1
        
        return low

if __name__ == "__main__":
    pass