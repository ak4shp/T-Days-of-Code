'''
Manchester coding.
If arr[i] and arr[i-1] are same, output will be 0 else 1.
'''

n = int(input())

prev = 0
ans = []
for i in range(n):
    nxt = int(input())
    if prev == nxt:
        ans.append(0)
    else:
        ans.append(1)
    prev = nxt
    
print(ans)