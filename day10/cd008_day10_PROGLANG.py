# cook your dish here
#!/usr/bin/env python3

# Codechef --> PROGLANG
# https://www.codechef.com/submit/PROGLANG
# Difficulty Rating:1001

'''
INPUT ->
3
1 2 2 1 3 4
3 4 2 1 4 3
1 2 1 3 2 4
OUTPUT ->
1
2
0
'''

for _ in range(int(input())):
    A, B, A1, B1, A2, B2 = map(int, input().split())
    
    if (A == A1 or A == B1) and (B == A1 or B == B1):
        print(1)
    elif (A == A2 or A == B2) and (B == A2 or B == B2):
        print(2)
    else:
        print(0)
