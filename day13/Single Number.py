#!/usr/bin/env python3

# LEETCODE  #136. Single Number
# https://leetcode.com/problems/single-number/
'''

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
'''

# Solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        hm = {}
        for i in nums:
            if i not in hm.keys():
                hm[i] = 1
            else:
                hm[i] += 1

        for i, v in hm.items():
            if v == 1:
                return i
