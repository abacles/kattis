def f(a, b, c, x):
	return a*x*x + b*x + c

def fit(x1, y1, x2, y2, x3, y3):
	a = ((y2-y3)*(x1-x2) - y1*(x2-x3) + y2*(x2-x3)) / ((x2*x2-x3*x3)*(x1-x2) - (x1*x1-x2*x2)*(x2-x3))
	b = (y1 - y2 - a*(x1*x1-x2*x2)) / (x1 - x2)
	c = y1 - a*x1*x1 - b*x1
	return a, b, c

for c in range(int(input())):
	xs, ys, xt, yt = [int(_) for _ in input().split()]
	n = int(input())
	obstacles = sorted([[int(_) for _ in input().split()] for i in range(n)])
	a = 0
	b = (yt - ys) / (xt - xs)
	c = ys - b * xs
	for i in range(n):
		if f(a, b, c, obstacles[i][0]) < obstacles[i][1]:
			a, b, c = fit(xs, ys, obstacles[i][0], obstacles[i][1], xt, yt)
	xmax = -b / (2*a) if a != 0 else 10001
	print(f(a, b, c, xmax) if xs <= xmax <= xt else max(ys, yt))
