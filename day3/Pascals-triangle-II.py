#!/usr/bin/env python3

# LEETCODE  #119 Pascal's Triangle II

'''
Input: rowIndex = 3
Output: [1,3,3,1]

Input: rowIndex = 0
Output: [1]

Input: rowIndex = 1
Output: [1,1]
'''


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        pascal = [[1], [1, 1]]  # initialize Base_rows of pascals triangle
        ri = rowIndex
        n = ri + 1
        
        # Edge cases
        if n == 1:
            return pascal[0]
        elif n == 2:
            return pascal[1]
        
        # Take the Base_row for generating other rows
        for i in range(1, n - 1):
            cur = pascal[i].copy()    # without copy() it will create reference
            res = cur.copy()
            
            # Actual Logic : result is sum of two terms of current 
            for j in range(1, len(cur)):
                res[j] = cur[j - 1] + cur[j]
            cur.append(1)    # For last term as 1
            res.append(1)
            pascal.append(res)

        return pascal[ri]

        