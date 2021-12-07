for c in range(int(input())):
	plus, minus = [int(_) for _ in input().split()]
	if plus >= minus and (plus - minus) % 2 == 0:
		a = (plus - minus) // 2
		b = plus - a
		print(max(a, b), min(a, b))
	else:
		print('impossible')
