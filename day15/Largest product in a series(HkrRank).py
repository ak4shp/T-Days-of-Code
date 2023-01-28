#!/bin/python3
# https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem?isFullScreen=true

"""
Sample Input:
        2
        10 5
        3675356291
        10 5
        2709360626

Sample Output:
        3150
        0
"""

import sys

def solve(N, K, num:str):
    mx_prod = 0
    
    for i in range(N-K+1):
        curr_prod = 1
        wind = num[i:i+K]
        if "0" in wind:
            continue
        
        for v in wind:
            curr_prod *= int(v)
            
        if curr_prod > mx_prod:
            mx_prod = curr_prod
            
    return mx_prod
        

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    
    print(solve(n, k, num))
