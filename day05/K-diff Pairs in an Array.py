#!/usr/bin/env python3

# LEETCODE  ##0532 K-diff Pairs in an Array
# https://leetcode.com/problems/k-diff-pairs-in-an-array/

"""
Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
"""


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        """ O(n2) | O(n) TLE!! """
        '''
        ct = 0
        # nums.sort()
        # print(nums)
        unique = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                # print(i, j)
                if i != j and nums[i] - nums[j] == k:
                    unique.add(nums[i])
        # print(unique)
        return len(unique)'''


        """ O(n) | O(n) """
        hm = {}
        ct = 0
        for i in nums:
            if i in hm.keys():
                hm[i] += 1
            else:
                hm[i] = 1

        for nm in hm:
            con1 = (k == 0 and hm[nm] > 1)
            con2 = (k > 0 and (nm+k) in hm)

            if con1 or con2:
                ct += 1

        return ct