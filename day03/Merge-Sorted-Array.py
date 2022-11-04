#!/usr/bin/env python3

# LEETCODE  #88 Merge Sorted Array

'''
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
'''


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        last = m + n - 1
      
        while m > 0 and n > 0:                   
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1
            
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

        return nums1