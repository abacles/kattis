import itertools, math

for c in range(int(input())):
	digits = input()
	primes = set()
	for i in range(1, len(digits)+1):
		for pm in itertools.permutations(digits, i):
			if pm[0] == '0': continue;
			x = int(''.join(pm))
			if x not in primes and x >= 2:
				for m in range(2, int(math.sqrt(x))+1):
					if x % m == 0:
						break
				else:
					primes.add(x)
	print(len(primes))
