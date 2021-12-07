def bfs(graph, horrors, n):
    INF = 9999
    dist = [INF] * n
    for h in horrors:
        dist[h] = 0
    q = horrors
    front = 0
    while front < len(q):
        v = q[front]
        front += 1
        for u in graph[v]:
            if dist[u] > dist[v] + 1:
                dist[u] = dist[v] + 1
                q.append(u)
    return dist

nmovies, nhorror, nsim = [int(_) for _ in input().split()]
horrors = [int(_) for _ in input().split()]

movie_graph = [[] for i in range(nmovies)]
for i in range(nsim):
    a, b = [int(_) for _ in input().split()]
    movie_graph[a].append(b)
    movie_graph[b].append(a)

hindex = bfs(movie_graph, horrors, nmovies)

max_index = 0
for i in range(nmovies):
    if hindex[i] > hindex[max_index]:
        max_index = i

print(max_index)
