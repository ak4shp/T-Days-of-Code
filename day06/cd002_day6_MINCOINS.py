#!/usr/bin/env python3

#  Codechef --> MINCOINS
#  https://www.codechef.com/submit/MINCOINS

'''
INPUT ->
3
50
15
8

OUTPUT ->
5
2
-1
'''


def solve(money):
    
    if money % 5 != 0:
        return -1
        
    tens = money // 10
    five = (money - tens * 10) // 5
    
    return tens + five
    

t =int(input())
while t:
    t -= 1
    money = int(input())
    print(solve(money))
    
    
    