# cook your dish here
#!/usr/bin/env python3

# Codechef --> FINALSUM
# https://www.codechef.com/submit/FINALSUM

'''
INPUT ->
2
5 3
1 3 4 4 2
1 5
3 4
2 2
1 2
4
1 1
1 1

OUTPUT ->
16
6
'''

'''Dont use solve fn below as this is a math problem. If subarr has even len the net of all +1, -1s will be zero. So only need to count how many subarr are of odd len and then add that count to sum(arr). That's it!!'''

# Time Limit Exceed
# def solve(Li, Ri, arr):
#     addr = -1
#     subr = 1
#     if Li % 2 == 0:
#         addr = 1
#         subr = -1
    
#     for i in range(Li-1, Ri):
        
#         if i % 2 != 0:
#             arr[i] += addr
#         else:
#             arr[i] += subr
#     return arr
    

for _ in range(int(input())):
    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    ct = 0
    for _ in range(Q):
        Li, Ri = map(int, input().split())
        
        """Just the math. no magic as +1, -1, +1, -1 is happening"""
        sub_size = Ri-Li+1
        if sub_size % 2 != 0:
            ct += 1

        # arr = solve(Li, Ri, arr) #TLE wali method
    print(sum(arr) + ct)