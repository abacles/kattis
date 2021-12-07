import sys

sys.setrecursionlimit(60000)

def dfs(g, i, v, prev):
    v[i] = True
    for j in g[i]:
        if j != prev and j != i and (v[j] or dfs(g, j, v, i)):
            return True
    return False

def cycle(g):
    visited = [False] * len(g)
    for i in range(len(g)):
        if not visited[i] and dfs(g, i, visited, -1):
            return True
    return False

def addpoint(m, p, n):
    if p not in m:
        m[p] = n
        n += 1
    return n

n = int(input())
sculpture = [None] * n
shadow = [None] * n
map3d = {}; map2d = {}
npoints3d = npoints2d = 0
for i in range(n):
    needle = [int(_) for _ in input().split()]
    sculpture[i] = [tuple(needle[:3]), tuple(needle[3:])]
    shadow[i] = [tuple(needle[:2]), tuple(needle[3:5])]
    npoints3d = addpoint(map3d, sculpture[i][0], npoints3d)
    npoints3d = addpoint(map3d, sculpture[i][1], npoints3d)
    npoints2d = addpoint(map2d, shadow[i][0], npoints2d)
    npoints2d = addpoint(map2d, shadow[i][1], npoints2d)


g3d = [[] for i in range(npoints3d)]
g2d = [set() for i in range(npoints2d)]
for i in range(n):
    g3d[map3d[sculpture[i][0]]].append(map3d[sculpture[i][1]])
    g3d[map3d[sculpture[i][1]]].append(map3d[sculpture[i][0]])
    g2d[map2d[shadow[i][0]]].add(map2d[shadow[i][1]])
    g2d[map2d[shadow[i][1]]].add(map2d[shadow[i][0]])

if cycle(g3d): print('True closed chains');
else: print('No true closed chains');
if cycle(g2d): print('Floor closed chains');
else: print('No floor closed chains')
