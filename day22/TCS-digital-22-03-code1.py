'''
Compare 2 arrays and output the elements of first array absent in second.
'''

M = 5
N = 6
a = [1, 2, 4, 5, 6]
b = [1, 2, 3, 7, 8, 9]

# First Method -->
res = []
for i in range(M):
    f = 1
    for j in range(N):
        if a[i] == b[j]:
            f = 0
            break
    if f == 1:
        res.append(a[i])     
print("First method: ", res)


# Second Method -->
res2 = []
for num in a:
    if num not in b:
        res2.append(num)
print("Second method: ", res2)




