import math

area, perim = [float(_) for _ in input().split()]
r = perim / (2*math.pi)
if math.pi*r*r >= area:
	print('Diablo is happy!')
else:
	print('Need more materials!')
