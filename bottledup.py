s, v1, v2 = [int(_) for _ in input().split()]
best = (1000000, 1000000)
for i in range(s//v1+1):
	if (s - i*v1) % v2 == 0:
		j = (s - i*v1) // v2
		if i + j < sum(best):
			best = (i, j)
if best == (1000000, 1000000):
	print('Impossible')
else:
	print('%d %d' % best)
