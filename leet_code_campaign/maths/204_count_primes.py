"""
204 Count Primes

Count the number of prime numbers less than a non negtaive number n

Input: 10
Output: 4
Explanation: 
There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Microsoft | Amazon | Oracle | Intel

Hash Table Math

Let's start with a isPrime function. 

To determine if a number is prime, 
we need to check if it is not 
divisible by any number less than n. 
The runtime complexity of isPrime 
function would be O(n) and hence 
counting the total prime numbers 
up to n would be O(n2). 
Could we do better?

As we know the number must not be 
divisible by any number > n / 2, 
we can immediately cut the 
total iterations half by dividing only 
up to n / 2. Could we still do better?

The Sieve of Eratosthenes is one of the
 most efficient ways to find all prime numbers
  up to n. But don't let that name scare you, 
I promise that the concept is surprisingly simple.

The Sieve of Eratosthenes 
uses an extra O(n) memory 
and its runtime complexity
 is O(n log log n). 
 
 For the more mathematically inclined readers,
  you can read more about its algorithm complexity
   on Wikipedia.
"""
import math


class Solution:
    def countPrimes(self, n: int) -> int:
       truth_table = n * [True]    
        for i in range(2, round(math.sqrt(n) + 1)):
            for j in range(i * i, n, i):
                truth_table[j] = False          
        primes = [i for i in range(2, n) if truth_table[i]]
        return len(primes)



if __name__ == "__main__":
    s = Solution()
    r = s.countPrimes(10)
    print(r)