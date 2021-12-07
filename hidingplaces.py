def dfs(r, c, d):
    dist[r][c] = d
    for dr, dc in [(1, 2), (2, 1)]:
        for sr in [-1, 1]:
            for sc in [-1, 1]:
                if 0 <= r+dr*sr < 8 and 0 <= c+dc*sc < 8 and d+1 < dist[r+dr*sr][c+dc*sc]:
                    dfs(r+dr*sr, c+dc*sc, d+1)

for t in range(int(input())):
    pos = input()
    r = int(pos[1]) - 1
    c = ord(pos[0]) - ord('a')
    dist = [[1000]*8 for _ in range(8)]
    dfs(r, c, 0)
    maxdist = max(dist[i][j] for i in range(8) for j in range(8))
    safe = [chr(ord('a')+j) + str(i+1) for i in range(8) for j in range(8) if dist[i][j] == maxdist]
    safe.sort(key = lambda x: (-int(x[1]), x[0]))
    print(maxdist, ' '.join(safe))
