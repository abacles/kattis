x, y = [int(_) for _ in input().split()]
if x > 0 and y > 0:
	lx = 250 - 31250 / x
	ry = 250 - 31250 / y
	print('%.2f %.2f' % (0 if 0 <= lx <= 250 else ry, lx if 0 <= lx <= 250 else 0))
elif 0 < x < 250:
	lx = 31250 / x
	rx = 31250 / (250 - x)
	print('%.2f %.2f' % (0 if 0 <= lx <= 250 else 250-rx, lx if 0 <= lx <= 250 else rx))
elif 0 < y < 250:
	ly = 31250 / y
	ry = 31250 / (250 - y)
	print('%.2f %.2f' % (ly if 0 <= ly <= 250 else ry, 0 if 0 <= ly <= 250 else 250-ry))
elif x == 0 and y == 0:
	print('125.00 125.00')
else:
	print('125.00 0.00' if x == 0 else '0.00 125.00')
