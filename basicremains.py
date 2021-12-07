def b2d(s, b):
	n = 0
	val = 1
	for digit in reversed(s):
		n += (ord(digit)-ord('0')) * val
		val *= b
	return n

def d2b(n, b):
	if n == 0: return '0'
	s = []
	while n > 0:
		s.append(n % b)
		n //= b
	return ''.join(str(_) for _ in s)[::-1]

while True:
	base, *pm = input().split()
	base = int(base)
	if base == 0: break;
	print(d2b(b2d(pm[0], base) % b2d(pm[1], base), base))
