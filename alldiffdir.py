import math

while True:
	n = int(input())
	if not n: break;
	finalpos = []; xsum = 0; ysum = 0
	for i in range(n):
		directions = input().split()
		x = float(directions[0]); y = float(directions[1])
		angle = 0
		for j in range(2, len(directions), 2):
			if directions[j] == 'start' or directions[j] == 'turn':
				angle += float(directions[j+1])
			else:
				x += math.cos(math.radians(angle)) * float(directions[j+1])
				y += math.sin(math.radians(angle)) * float(directions[j+1])
		finalpos.append((x, y))
		xsum += x; ysum += y
	xavg = xsum / n; yavg = ysum / n
	maxdist = 0
	for i in range(n):
		maxdist = max(maxdist, math.hypot(finalpos[i][0]-xavg, finalpos[i][1]-yavg))
	print(xavg, yavg, maxdist)
