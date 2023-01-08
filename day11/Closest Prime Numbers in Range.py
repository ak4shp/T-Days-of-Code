#!/usr/bin/env python3

# LEETCODE  #2523 Closest Prime Numbers in Range
# https://leetcode.com/problems/closest-prime-numbers-in-range/

'''
Example 1:

Input: left = 10, right = 19
Output: [11,13]
Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
Since 11 is smaller than 17, we return the first pair.

Example 2:

Input: left = 4, right = 6
Output: [-1,-1]
Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
'''


class Solution:
    def isPrime(self, num):
        if num < 2:
            return False
        if num % 2 == 0:
            return num == 2
            
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True
        
        
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        primes = []
        ans = [-1, -1]
        diff = float('inf')
        for num in range(left, right + 1):
            if self.isPrime(num):
                primes.append(num)
          
                for i in range(1, len(primes)):
                    df = primes[i] - primes[i-1]
                    if df < diff:
                        diff = df
                        ans[0] = primes[i-1]
                        ans[1] = primes[i]
                        if diff <= 2:
                            return ans
                
        return ans