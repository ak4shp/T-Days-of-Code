# cook your dish here
# https://www.codechef.com/problems/APPENDOR

'''
input:
4
4 15
3 5 6 2
3 8
1 2 1
1 1
0
5 7
1 2 4 2 1

output:
8
-1
1
0
'''


def solve(res, x):
    # Alternate Approach ->
    # Convert to binary and compare each bit
    # binx= list(bin(x).replace("b", ""))
    # bin_res = list(bin(res).replace("b", ""))
    # bin_ans = []
    
    if x == res:
        return 0
    for i in range(res+1):
        if i | x == res:
            return i
            
    return -1
    


t = int(input())
while t:
    t -= 1
    n, y = map(int, input().split())
    arr = list(map(int, input().split()))
    
    arr_or = 0
    for num in arr:
        arr_or = arr_or | num
        
    if arr_or <= y:
        print(solve(y, arr_or))
        
    else:
        print(-1)
    
    