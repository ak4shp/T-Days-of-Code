#!/usr/bin/env python3

# LEETCODE   #1276 Number of Burgers with No Waste of Ingredients


'''
Input: tomatoSlices = 16, cheeseSlices = 7
Output: [1,6]

Input: tomatoSlices = 17, cheeseSlices = 4
Output: []

Input: tomatoSlices = 4, cheeseSlices = 17
Output: []

'''

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        t = tomatoSlices
        s = cheeseSlices
        if t == 0 and s == 0:
            return [0, 0]
        
        if (t%2 != 0) or t <= s:
            return []
        
        
        x = t/2 - s
        y = s - x
        
        if x == int(x) and y == int(y) and x >= 0 and y >= 0:
            return [int(x), int(y)]
        else:
            return []
