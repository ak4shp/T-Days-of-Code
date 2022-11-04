#!/usr/bin/env python3

# LEETCODE  #217
'''
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: True

Input: nums = [1,2,3,4]
Output: False
'''


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        '''Way 1 : time -> O(n log n) | space -> O(1)'''
        # nums.sort()   # O(n log n)
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False
        
        '''Way 2 : time -> O(n) | space -> O(n)'''
        hm = {}
        for i in nums:
            if i in hm.keys():
                return True
            else:
                hm[i] = 1
        return False