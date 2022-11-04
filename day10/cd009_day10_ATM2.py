# cook your dish here
#!/usr/bin/env python3

# Codechef --> ATM2
# https://www.codechef.com/submit/ATM2
# Difficulty Rating:1001


'''
INPUT ->
2
5 10
3 5 3 2 1
4 6
10 8 6 4
OUTPUT ->
11010
0010
'''

def solve(N, K, arr):
    ans = ""
    rem = K
    
    for m in arr:
        if m <= rem:
            ans += "1"
            rem -= m
        else:
            ans += "0"
            
    return ans
    
    
for _ in range(int(input())):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    
    print(solve(N, K, arr))
    