# cook your dish here
# https://www.codechef.com/problems/CNDY

'''
Input:
4
3
4 8 4 6 7 3
3
4 8 6 8 7 8
2
2 4 5 3
4
8 7 9 8 4 6 2 8

output:
Yes
No
Yes
No
'''


t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    ans = "Yes"
    for i in range(2 * n):
        ct = 1
        for j in range(i+1, 2 * n):
            if arr[i] == arr[j]:
                ct += 1
                if ct >= 3:
                    ans = "No"
                    break
        if ans == "No":
            break
        
    print(ans)