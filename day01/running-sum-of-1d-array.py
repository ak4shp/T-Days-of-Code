#!/usr/bin/env python3

# LEETCODE #1480
'''
INPUT ->  [3,1,2,10,1]
OUTPUT -> [3,4,6,16,17]
'''

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
        