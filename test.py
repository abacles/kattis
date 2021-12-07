r, c = [int(x) for x in input().split()]
input()
w = [[0] * c] + [[int(x) for x in input().split()] for _ in range(r)] + [[0] * c]
input()

INF = r * 9
e = [[0] * c] + [[INF] * c for _ in range(r+1)]

while True:
    ne = [l[:] for l in e]
    for i in range(1, r+2):
        for j in range(c):
            if i + 1 <=r+1:
                ne[i][j] = max(0, min(ne[i][j], e[i+1][j] + w[i][j]))
            if i - 1 >=0:
                ne[i][j] = max(0, min(ne[i][j], e[i-1][j] + w[i][j]))
            if j + 1 < c:
                ne[i][j] = max(0, min(ne[i][j], e[i][j+1] + w[i][j]))
            if j - 1 >=0:
                ne[i][j] = max(0, min(ne[i][j], e[i][j-1] + w[i][j]))

    if e == ne:
        break
    e = ne

print(min(ne[-1]))
