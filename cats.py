import heapq

def mst(g, n):
    q = [(0, 0)]
    d = {x: 10000 for x in range(n)}
    mst = 0
    while len(q) > 0:
        w, v = heapq.heappop(q)
        if d[v] == 0: continue;
        d[v] = 0
        mst += w
        for j in range(n):
            if d[j] > 0 and g[v][j] < d[j]:
                heapq.heappush(q, (g[v][j], j))
                d[j] = g[v][j]
    return mst

for c in range(int(input())):
    milk, ncats = [int(_) for _ in input().split()]
    dist = [[0] * ncats for _ in range(ncats)]
    for i in range(ncats * (ncats-1) // 2):
        a, b, d = [int(_) for _ in input().split()]
        dist[a][b] = dist[b][a] = d
    print('yes' if milk - mst(dist, ncats) >= ncats else 'no')
