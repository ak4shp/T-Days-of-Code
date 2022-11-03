# cook your dish here
#!/usr/bin/env python3

# Codechef --> DIET
# https://www.codechef.com/submit/DIET

'''
INPUT ->
3
4 5
7 3 6 5
3 4
3 10 10
3 4
8 1 1

OUTPUT ->
YES
NO 1
NO 3
'''


def solve(n, need, diets):
    rem = 0
    for i in range(1, n+1):
        to_eat = rem + diets[i-1]
        rem = to_eat - need
        # print(i, to_eat, rem)
        if rem < 0:
            return "NO " + str(i)
    return "YES"
    
    
for _ in range(int(input())):
    n, k = map(int, input().split())
    diet_food = list(map(int, input().split()))
    
    print(solve(n, k, diet_food))