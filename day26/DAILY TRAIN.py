# https://www.codechef.com/problems/DAILY?tab=statement


def fact(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    return a 


def ncr(n, r):
    return fact(n) // (fact(n - r) * fact(r))
    
x, n = map(int, input().split())

result = 0

for i in range(n):
    s = input()
    j = 0
    for i in range(0, 36, 4):
        c = (s[i:i+4] + s[52-j:54-j]).count('0')
        j += 2
        if c >= x:
            result += ncr(c, x)
print(result)