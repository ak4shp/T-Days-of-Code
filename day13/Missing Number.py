#!/usr/bin/env python3

# LEETCODE  #268. Missing Number

# https://leetcode.com/problems/missing-number/description/

'''

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 
'''

# Solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) + 1
        for i in range(n):
            if i == n - 1 or i != nums[i]:
                return i
