#!/bin/python3

import math
import os
import random
import re
import sys


# https://www.hackerrank.com/test/4nahpm20m33/questions/di1dm3kpigj

"""
Flipping the matrix:  
Maximise sum at upper left quadrant of that matrix by reversing any row or column any number of times 
"""

# Complete the 'flippingMatrix' function below.
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.

"""
matrix = [[1, 2], [3, 4]]
1 2 
3 4

reverse R1 ->
1 2
4 3

reverse C0 ->
4 2
1 3

hence, answer is 4
"""


def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)//2
    
    v = 0
    for i in range(n):
        for j in range(n):
            corner_vals = [] 
            corner_vals.append(matrix[i][j]) # current matrix
            corner_vals.append(matrix[2 * n - 1 - i][j])  # bottom left
            corner_vals.append(matrix[i][2 * n - 1- j]) # top right
            corner_vals.append(matrix[2* n - 1 - i][2 * n - 1- j]) # bottom right
            # print(corner_vals)
            maxv = max(corner_vals)
            #print(corner_val)
            #print(max(l))
            
            v += maxv

    return v

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
