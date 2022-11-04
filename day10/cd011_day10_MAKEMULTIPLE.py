# cook your dish here
#!/usr/bin/env python3

# Codechef --> MAKEMULTIPLE
# https://www.codechef.com/submit/MAKEMULTIPLE
# Difficulty Rating:1163

'''
INPUT ->
3
3 6
4 14
9 10
OUTPUT ->
YES
YES
NO
'''

for _ in range(int(input())):
    a, b = map(int, input().split())
    
    # d = b - a
    # if d == 0 or a <= d:
    
    if a == b or a <= b/2:
        print("YES")
    else:
        print("NO")
        
        