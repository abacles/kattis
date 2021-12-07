def solve(left, right, nvars):
    for svd in range(nvars):
        div = left[svd][svd]
        for i in range(nvars):
            left[svd][i] /= div
        right[svd] /= div
        for i in range(nvars):
            if i != svd:
                mult = -left[i][svd] / left[svd][svd]
                for j in range(nvars):
                    left[i][j] += mult * left[svd][j]
                right[i] += mult * right[svd]
    return right

nclears, npaths = [int(_) for _ in input().split()]
forest = [[] for _ in range(nclears)]
for _ in range(npaths):
    a, b = [int(_) for _ in input().split()]
    forest[a].append(b)
    forest[b].append(a)
coef = [[0]*nclears for _ in range(nclears)]
cv = [1] * nclears

coef[-1][-1] = 1 # z = 0
cv[-1] = 0

for i in range(nclears-1):
    coef[i][i] = 1
    avgcoef = len(forest[i])
    for c in forest[i]:
        coef[i][c] -= 1 / avgcoef

print(solve(coef, cv, nclears)[0])
