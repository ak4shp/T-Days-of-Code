# cook your dish here
# https://www.codechef.com/problems/AVG

'''
input:
3
3 3 4
2 7 3
3 1 4
7 6 5
3 3 4
2 8 3

output:
4
-1
-1
'''

t = int(input())
while t:
    t -= 1
    n, k, v = map(int, input().split())
    arr = list(map(int, input().split()))
    
    x = ((n+k)*v - sum(arr))
    
    ans = x // k
    
    if x > 0 and x % k == 0:
        print(ans)
    else:
        print(-1)