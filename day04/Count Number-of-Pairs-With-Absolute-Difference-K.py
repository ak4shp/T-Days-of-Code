#!/usr/bin/env python3

# LEETCODE  #2006 Count Number of Pairs With Absolute Difference K


'''
Input: nums = [3,2,1,5,4], k = 2
Output: 3

Input: nums = [1,3], k = 3
Output: 0

Input: nums = [1,2,2,1], k = 1
Output: 4
'''

class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ct = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k:
                    ct += 1
        return ct

        