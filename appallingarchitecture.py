r, c = [int(_) for _ in input().split()]
blueprint = [input() for _ in range(r)]
xsum = 0; n = 0
for i in range(r):
	for j in range(c):
		if blueprint[i][j] != '.':
			xsum += j
			n += 1

left = -1
for j in range(c):
	if blueprint[-1][j] != '.' and left == -1: left = j;
	if blueprint[-1][j] != '.': right = j;

xcenter = round(xsum / n)
if xcenter < left: print('left');
elif left <= xcenter <= right: print('balanced');
else: print('right');
