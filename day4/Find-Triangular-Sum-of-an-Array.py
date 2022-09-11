#!/usr/bin/env python3

# LEETCODE  #2221 Find Triangular Sum of an Array


'''
Input: nums = [1,2,3,4,5]
Output: 8

Input: nums = [5]
Output: 5
'''


class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Edge cases
        if n == 1:
            return nums[0] % 10
        elif n == 2:
            return (nums[0] + nums[1]) % 10
        
        # Take the Base_row for generating other rows
        for j in range(n - 1):
            res = []            # Dummy array
            for i in range(len(nums) - 1):
                curr = (nums[i] + nums[i + 1]) % 10   # Logic
                res.append(curr)
                
            nums = res.copy()   # Reduced arry for each iteration
        
        return nums[0]
            