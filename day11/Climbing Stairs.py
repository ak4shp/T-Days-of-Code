#!/usr/bin/env python3

# LEETCODE  #70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

'''
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1

        for i in range(n):
            tmp = a
            a = b
            b = tmp + b

        return b