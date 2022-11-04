#!/usr/bin/env python3

# Codechef --> ZOOZ
# https://www.codechef.com/submit/ZOOZ

'''
INPUT ->
2
4
3

OUTPUT ->
1001
010
'''


def get_zooz(n):
    res = ""
    addon = "10"
    
    if n == 3:
        return "010"
    
    if n % 2 == 0:
        multiplier = (n-2)//2
        res += addon*multiplier
        res += "01"
        
    else:
        multiplier = (n-1)//2
        res += addon*multiplier
        res += "1"
    return res
  
  
''' This function <get_zooz_2>implements what was asked. It is not necessary that '01' or '01' should be consecutive. So,'100' has 2 set of '10's-> at (idx 0 + idx 1) and (idx 0 + idx 2). If they need to be consecutive use <get_zooz> function above.'''

def get_zooz_2(n):
    res = "1"
    res += "0"*(n-2)
    res += "1"
    
    return res
    
    
t = int(input())
while t:
    t -= 1
    n = int(input())
    print(get_zooz_2(n))
    
    
    
    
    
    
    
    