#!/usr/bin/env python3

# LEETCODE  #118 Pascal's Triangle

'''
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Input: numRows = 1
Output: [[1]]
'''


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pascal = [[1], [1, 1]]  # initialize Base_rows of pascals triangle
        n = numRows
        
        # Edge cases
        if n == 1:
            return [pascal[0]]
        elif n == 2:
            return pascal
        
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

        return pascal