#!/usr/bin/env python3

# LEETCODE  #283. Move Zeroes


'''
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # move zeros in ending --> 
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1


        # move zeros in starting -->
        """
        j = n -1 
        for i in range(n-1, -1, -1):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j -= 1
        """