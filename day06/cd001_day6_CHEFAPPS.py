#!/usr/bin/env python3

# Codechef --> CHEFAPPS
# https://www.codechef.com/submit/CHEFAPPS

'''
INPUT ->
4
10 1 2 3
9 4 5 1
15 5 10 15
100 20 30 75

OUTPUT ->
0
1
2
1
'''

def solve(mem, a, b, need):
    unused = mem - (a + b)
    if unused >= need:
        return 0
    elif unused + max(a, b) >= need:
        return 1
    else:
        return 2
        
t = int(input())
while t:
    t -= 1
    mem, a, b, need = map(int, input().split())
    print(solve(mem, a, b, need))
    
    
    
    