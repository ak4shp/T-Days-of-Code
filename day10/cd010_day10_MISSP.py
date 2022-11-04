# cook your dish here
#!/usr/bin/env python3

# Codechef --> MISSP
# https://www.codechef.com/submit/MISSP
# Difficulty Rating:1012

'''
INPUT ->
1
3
1 
2
1
OUTPUT ->
2
'''

def solve(n, doll):
    doll.sort()
    if n %2 != 0:
        doll.append(0)
    for i in range(0, n, 2):
        if doll[i] != doll[i+1]:
            return doll[i]
    
    
for _ in range(int(input())):
    n = int(input())
    doll = []
    for _ in range(n):
        doll.append(int(input()))
        
    print(solve(n , doll))