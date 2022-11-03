# cook your dish here
#!/usr/bin/env python3

# Codechef --> SLOWSOLN
# https://www.codechef.com/submit/SLOWSOLN

'''
INPUT ->
4
10 100 200
3 10 100
1000 1000 2200
100 100 100

OUTPUT ->
20000
300
2040000
10000
'''


def solve(test, num, mx):
    rem = mx
    curr = num
    arr = []
    while test:
        test -= 1
        curr = num
        if rem < num:
            curr = rem
        # print("\nrem: ", rem, "curr: ", curr)
        rem -= curr
        arr.append(curr)
        if rem <= 0:
            break
    # print(arr)
    return sum((map(lambda x: x**2, arr)))
    
    
for _ in range(int(input())):
    T, N, sumN = map(int, input().split())
    print(solve(T, N, sumN))
            