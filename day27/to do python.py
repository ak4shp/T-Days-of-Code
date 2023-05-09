t = 3
4   -> 2
5   -> 5
6   -> 3

def solve(n):
    ls = []
    val = [False]*n
    for i in range(1, n+1):
        for j in range(i, n+1):
            df = abs(i-j)
            if df > 1 and n % df == 0:
                ls.append([i, j])
    op = 0

    if len(ls) == 0:
        return n
        
    for i in range(1, n+1):
        if not val[i-1]:
            for ct in ls:
                for j in ct:
                    if j == i:
                        val[j] = True
                        op += 1
    return op
                
    

t = int(input())
while t:
    t -= 1 
    n = int(input())
    res = solve(n)
    print(res)
    