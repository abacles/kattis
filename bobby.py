factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

def choose(sm, big):
	top = 1
	for i in range(big, big-sm, -1):
		top *= i
	return top // factorial[sm]

for c in range(int(input())):
	r, s, x, y, w = [int(_) for _ in input().split()]
	k = s - r + 1
	top = 0
	bot = s ** y
	for i in range(x, y+1):
		top += (k ** i) * ((s-k) ** (y-i)) * choose(i, y)
	print('yes' if w * top > bot else 'no')
