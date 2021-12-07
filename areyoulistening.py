import math

cx, cy, n = [int(_) for _ in input().split()]
dist = []
for i in range(n):
	x, y, r = [int(_) for _ in input().split()]
	dist.append(max(0, math.hypot(cx-x, cy-y) - r))

dist.sort()
print(int(dist[2]))
