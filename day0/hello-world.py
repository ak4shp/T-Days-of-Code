# This file is only for testing codes :)

def subset(a):
    ss = []
    mn = 0
    mx = 0
    res = []
    for i in range(len(a)):
        for j in range(i, len(a)):
            ss.append(a[i:j + 1])

    for i in ss:
        mn = min(i)
        mx = min(i)
        res.append(mn * mx)

    return min(res), max(res)


print(subset([1, 2, 3, 4, 5]))

print(subset([-12, -10, 0]))