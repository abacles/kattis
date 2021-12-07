import heapq

def mandist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def dijkstra(g, n, k):
    dist = [[-1] * n for i in range(n)]
    q = []
    for i, j in g[0]:
        dist[i][j] = 0
        q.append((0, 0, i, j))
    while len(q) > 0:
        d, x, i, j = heapq.heappop(q)
        if d > dist[i][j]: continue;
        if x == k-1: return d
        for ip, jp in g[x+1]:
            md = mandist((i, j), (ip, jp))
            if d + md < dist[ip][jp] or dist[ip][jp] == -1:
                dist[ip][jp] = d + md
                heapq.heappush(q, (d + md, x+1, ip, jp))
    return -1
    

n, k = [int(_) for _ in input().split()]
x_squares = [[] for i in range(k)]

for i in range(n):
    row = [int(_) for _ in input().split()]
    for j in range(n):
        x_squares[row[j]-1].append((i, j))

print(dijkstra(x_squares, n, k))
