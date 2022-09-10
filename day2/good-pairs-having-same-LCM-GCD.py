#!/usr/bin/env python3

# CODECHEF : EQPAIR
'''
Print count of good pairs in an array.

Input:
5    # no. of test_cases
2    # length of array
5 9  # array
5
1 5 5 5 9
8
2 5 5 2 9 9 9 12
4
12 12 18 18
5
12 15 10 5 9

Output:
0
3
5
2
0
'''

t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    hm = {}
    c = 0
    
    for i in arr:
        if i not in hm.keys():
            hm[i] = 1
        else:
            hm[i] += 1
            
    for k, v in hm.items():
        if v > 1:
            s = (v * (v - 1)) // 2
            c += s
    print(c)
    
    
'''Using these two functions gives TLE :)'''
# def find_gcd(a, b):
#     n, m = a, b
#     while(n != 0):
#         t = n
#         n = m % n
#         m = t
#     gcd = m
#     return gcd
    
    
# def find_lcm(a, b):
#     lcm = int(a * b / find_gcd(a, b))
#     return lcm
    
