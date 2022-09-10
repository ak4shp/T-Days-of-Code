#!/usr/bin/env python3

# LEETCODE  #350 Intersection of Two Arrays II
'''
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9] or [9, 4] both accepted

Input: nums1 = [4,9,4,5], nums2 = [9,4,9,8,4]
Output: [9, 4, 4] or [4, 9, 4] or [4, 4, 9] all accepted
'''


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        d = {}
        res = []

        opr = nums1
        opr2 = nums2
        if len(nums1) > len(nums2):
            opr = nums2
            opr2 = nums1
        
        for i in range(len(opr)):
            ele = opr[i]
            x = d.get(ele, False)
            if not x:
                d[ele] = 1
            else:
                d[ele] += 1
                
        for i in range(len(opr2)):
            ele = opr2[i]
            x = d.get(ele, False)
            if x:
                d[ele] -= 1
                res.append(ele)
                
        return res