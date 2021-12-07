import sys

dx = dy = left = right = up = down = 0
pos = [(0, 0)]
for line in sys.stdin:
	if line == 'up\n': dy -= 1
	elif line == 'down\n': dy += 1
	elif line == 'left\n': dx -= 1
	else: dx += 1
	pos.append((dy, dx))
	up = max(up, -dy)
	down = max(down, dy)
	left = max(left, -dx)
	right = max(right, dx)

pathmap = [[' ']*(left+right+1) for _ in range(up+down+1)]
for p in pos:
	pathmap[up+p[0]][left+p[1]] = '*'
pathmap[up][left] = 'S'
pathmap[up+pos[-1][0]][left+pos[-1][1]] = 'E'
print('#' * (left+right+3))
for row in pathmap:
	print('#' + ''.join(row) + '#')
print('#' * (left+right+3))
