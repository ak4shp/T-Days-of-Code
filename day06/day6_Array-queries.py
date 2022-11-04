'''
Question :- https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/array-queries-again-7948f256/

'''



def swap(A, B, opr, i, j):
    if opr == 1:
        tmp = A[i]
        A[i] = B[j]
        B[j] = tmp
    elif opr == 2:
        A[i], A[j] = A[j], A[i]
    elif opr == 3:
        B[i], B[j] = B[j], B[i]


def evaluate(A, B, N, M):
    eval_ans = 0
    for i in range(N):
        for j in range(M):
            eval_ans += A[i]*B[j]*(i+1 + j+1)%998244353
    return eval_ans


def array_queries (N, M, A, B, Q, queries):
    res = []
    # print("A, B ", A, B)
    res.append(evaluate(A, B, N, M))
    for qr in queries:
        opr = qr[0]
        qi = qr[1] -1
        qj = qr[2] -1
        
        swap(A, B, opr, qi, qj)
        res.append(evaluate(A, B, N, M))
    return res



T = int(input())
for _ in range(T):
    N = int(input())
    M = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Q = int(input())
    queries = [list(map(int, input().split())) for i in range(Q)]

    out_ = array_queries(N, M, A, B, Q, queries)
    print (' '.join(map(str, out_)))