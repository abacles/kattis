import math

def concave(p1, p2, p3):
	return (p1[0]-p2[0])*(p3[1]-p2[1]) > (p1[1]-p2[1])*(p3[0]-p2[0])

def convex_hull(p):
	midx = midy = 0
	for i in range(len(p)):
		midx += p[i][0] / len(p)
		midy += p[i][1] / len(p)
	tmp = [math.atan2(p[i][1]-midy, p[i][0]-midx) for i in range(len(p))]
	o = sorted(list(range(len(p))), key = lambda x: tmp[x])
	hull = [o[0], o[1]]
	for i in range(2, len(p)):
		while len(hull) >= 2 and concave(p[hull[-2]], p[hull[-1]], p[o[i]]):
			hull.pop()
		hull.append(o[i])
	check = True
	hull_start = 0
	while check:
		check = False
		if concave(p[hull[-2]], p[hull[-1]], p[hull[hull_start]]):
			hull.pop()
			check = True
		if concave(p[hull[-1]], p[hull[hull_start]], p[hull[hull_start+1]]):
			hull_start += 1
			check = True
	area = 0
	for i in range(hull_start, len(hull)):
		area += p[hull[i]][0] * p[hull[i+1 if i+1<len(hull) else hull_start]][1] - p[hull[i+1 if i+1<len(hull) else hull_start]][0] * p[hull[i]][1]
	return 0.5 * area

for c in range(int(input())):
	n = int(input())
	points = []
	area = 0
	for i in range(n):
		x, y, w, h, v = [float(_) for _ in input().split()]
		d = 0.5 * math.hypot(w, h)
		area += w * h
		for dx in (-1, 1):
			for dy in (-1, 1):
				theta = math.atan2(dy*h, dx*w)
				points.append((x + d * math.cos(theta - math.radians(v)), y + d * math.sin(theta - math.radians(v))))
	print('%.1f %%' % (area / convex_hull(points) * 100))
