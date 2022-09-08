#!/usr/bin/env python3

# LEETCODE # 724
'''
INPUT -> [1,7,3,6,5,6]
OUTPUT -> 3
'''

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sm = 0
        for i in nums:
            sm += i
        leftsm = 0
        for i in range(len(nums)):
            remsm = sm - leftsm - nums[i]
            if leftsm == remsm:
                return i
            leftsm += nums[i]
        return -1
