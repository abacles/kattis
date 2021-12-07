def rot(s, d = 1):
	return (s + d + 6) % 6

def neighbor(c, s, l, w, f, r):
	if (s < 2 and l[c] == 0) or ((s == 3 or s == 4) and l[c] == 2*r-2):
		return None
	if s == 0: # northwest
		t = c - w[l[c]] if l[c] < r else c - w[l[c]-1]
	elif s == 1: # northeast
		t = (c - w[l[c]] if l[c] < r else c - w[l[c]-1]) + 1
	elif s == 2: # east
		return c + 1 if c + 1 < f[l[c]] + w[l[c]] else None
	elif s == 3: # southeast
		t = c + w[l[c]+1] if l[c] < r-1 else c + w[l[c]]
	elif s == 4: # southwest
		t = (c + w[l[c]+1] if l[c] < r-1 else c + w[l[c]]) - 1
	else: # west
		return c - 1 if c - 1 >= f[l[c]] else None
	if s < 2:
		return t if f[l[c]-1] <= t < f[l[c]-1] + w[l[c]-1] else None
	else:
		return t if f[l[c]+1] <= t < f[l[c]+1] + w[l[c]+1] else None

r, k = [int(_) for _ in input().split()]
house = [int(_) for _ in input().split()]
n = r**3 - (r-1)**3

level = []
width = list(range(r, r+r-1)) + list(range(r+r-1, r-1, -1))
for l in range(len(width)):
	level.extend([l] * width[l])
first = [0]
for l in range(len(width)-1):
	first.append(first[-1] + width[l])

walls = [[0]*6 for _ in range(n)]
for c in house:
	for i in range(6):
		nbr = neighbor(c-1, i, level, width, first, r)
		if nbr != None and walls[nbr][rot(i, 3)] > 0:
			walls[nbr][rot(i, 3)] += 1
		else:
			walls[c-1][i] += 1

cell = orig = min(house) - 1
side = 0
perim = 0
while True:
	perim += 1
	lnbr = neighbor(cell, side, level, width, first, r)
	rnbr = neighbor(cell, rot(side), level, width, first, r)
	if walls[cell][rot(side)] == 1 or (rnbr != None and walls[rnbr][rot(side, 4)] == 1):
		side = rot(side)
	elif lnbr != None and walls[lnbr][rot(side, 2)] == 1 or rnbr != None and walls[rnbr][rot(side, -1)] == 1:
		cell = rnbr
		side = rot(side, -1)
	else:
		print('no no no') 
	if cell == orig and side == 0:
		break
print(perim)
