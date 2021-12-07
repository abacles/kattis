n = int(input())
buses = sorted([int(_) for _ in input().split()])
i = 0
sign = []
while i < n:
	if i < n - 2:
		j = i + 1
		while j < n and buses[j] == buses[j-1] + 1:
			j += 1
		if j >= i + 3:
			sign.append('%d-%d' % (buses[i], buses[j-1]))
			i = j
			continue
	sign.append(str(buses[i]))
	i += 1
print(' '.join(sign))
