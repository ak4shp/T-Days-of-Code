# https://www.codechef.com/problems/RECNDSTR?tab=statement
def L(s):
    return s[1:len(s)]+s[0]
    
def R(s):
    return s[-1]+s[:-1]


t = int(input())
while t:
    t -= 1
    s = input()
    
    res = "YES" if L(s)==R(s) else "NO"
    print(res)
        