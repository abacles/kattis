from collections import deque
c, r = [int(_) for _ in input().split()]
alt = [[1000] + [int(_) for _ in input().split()] + [1000] for i in range(r)]
alt = [[1000]*(c+2)] + alt + [[1000]*(c+2)]
drain = set()
q = deque()
for i in range(1, r+1):
    for j in range(1, c+1):
        if alt[i][j] > min(alt[i-1][j], alt[i+1][j], alt[i][j-1], alt[i][j+1]):
            drain.add((i, j))
            q.append((i, j))
while q:
    i, j = q.popleft()
    for d in [-1, 1]:
        if alt[i+d][j] == alt[i][j] and (i+d, j) not in drain:
            drain.add((i+d, j))
            q.append((i+d, j))
        if alt[i][j+d] == alt[i][j] and (i, j+d) not in drain:
            drain.add((i, j+d))
            q.append((i, j+d))
print(r*c - len(drain))
