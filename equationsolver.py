# Ax = b

def zero(c):
    return -1e-15 <= c <= 1e-15

def solv(A, n):
    for i in range(n):
        k = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[k][i]): k = j;
        if zero(A[k][i]):
            for j in range(n):
                A[j][i] = 0
            continue
        A[i], A[k] = A[k], A[i]
        for j in range(n):
            if i != j:
                f = A[j][i] if not zero(A[j][i]) else 0
                for k in range(n+1):
                    A[j][k] -= f * A[i][k] / A[i][i]
                    if k == i:
                        A[j][k] = 0.0

while True:
    n = int(input())
    if not n: break;
    A = [[float(_) for _ in input().split()] for _ in range(n)]
    b = [float(_) for _ in input().split()]
    A = [A[i] + [b[i]] for i in range(n)]
    solv(A, n)
    sol = 1
    for i in range(n):
        j = 0
        while j <= n and zero(A[i][j]):
            j += 1
        if j >= n:
            sol = 0 if j == n else 100
    if sol == 1:
        x = [A[i][-1]/A[i][i] for i in range(n)]
        print(' '.join([str(_) for _ in x]))
    else:
        print('inconsistent' if not sol else 'multiple')
