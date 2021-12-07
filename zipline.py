import math

def qsolv(a, b, c):
	if a == 0:
		return (-c / b, )
	tmp = math.sqrt(b*b - 4*a*c)
	return (-b+tmp)/(2*a), (-b-tmp)/(2*a)

def ziplength(x, a, b, w):
	return math.sqrt(a*a+x*x) + math.sqrt(b*b+(w-x)**2)

for c in range(int(input())):
	w, g, h, r = [int(_) for _ in input().split()]
	a = g - r
	b = h - r
	longer = max(ziplength(_, a, b, w) for _ in qsolv(a*a-b*b, -2*a*a*w, a*a*w*w) if 0 <= _ <= w) if not r == g == h else w
	print(math.hypot(w, g-h), longer)
