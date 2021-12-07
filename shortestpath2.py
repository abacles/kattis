import heapq, math

inf = int(1e9)

def dijkstra(g, n, src):
    dist = [(inf if v!=src else 0, v) for v in range(n)]
    heapq.heapify(dist)
    distfinal = [inf if v!=src else 0 for v in range(n)]
    visited = [False] * n
    for i in range(n):
        d, v = heapq.heappop(dist)
        while visited[v]: d, v = heapq.heappop(dist);
        if d == inf: break;
        visited[v] = True
        for e in g[v]:
            if e[2] == 0 and d > e[1]: continue;
            if d <= e[1]:
                t1 = e[1] + e[3]
            else:
                t1 = e[1] + math.ceil((d-e[1])/e[2]) * e[2] + e[3]
            if t1 < distfinal[e[0]]:
                heapq.heappush(dist, (t1, e[0]))
                distfinal[e[0]] = t1
    return distfinal

while True:
    n, m, q, src = [int(_) for _ in input().split()]
    if n == m == q == src == 0: break;
    g = [[] for _ in range(n)]
    for i in range(m):
        u, v, t0, p, d = [int(_) for _ in input().split()]
        g[u].append((v, t0, p, d))
    dist = dijkstra(g, n, src)
    for i in range(q):
        v = int(input())
        print(dist[v] if dist[v] < inf else 'Impossible')
    print()
