#!/usr/bin/env python3

# LEETCODE #13

class Solution:
    def romanToInt(self, s: str) -> int:
        hm = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        n = len(s)
        res = hm[s[n - 1]]
        for i in range(n - 2, -1, -1):
            left = hm[s[i]]
            right = hm[s[i + 1]]

            if left >= right:
                res += left
            else:
                res -= left

        return res

