#!/usr/bin/env python3

# LEETCODE #53
'''
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [5,4,-1,7,8]
Output: 23

Input: nums = [1]
Output: 1
'''


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        mx = nums[0]
        curr = 0
        
        for i in nums:
            if curr < 0:
                curr = 0
            curr += i
            mx = max(mx, curr)
            
        return mx
        