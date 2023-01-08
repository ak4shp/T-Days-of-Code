#!/usr/bin/env python3

# LEETCODE  #27. Remove Element
# https://leetcode.com/problems/remove-element/

'''
Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """ O(n) | O(n) """
        
        # ct = 0
        # nums2 = nums.copy()
        # n = len(nums2)
        # for i in range(n):
        #     if nums2[i] == val:
        #         ct += 1
        #         nums.remove(nums2[i])
        # return int(n - ct)

        """ O(n) | O(1) """
        j=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        return j
