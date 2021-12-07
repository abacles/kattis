cap = int(input())
bus = [0] * 400000
for i in range(1, 75):
	for j in range(i, 75):
		if i**3 + j**3 > 400000:
			break
		bus[i**3+j**3-1] += 1
for i in range(cap, 0, -1):
	if bus[i-1] >= 2:
		print(i)
		break
else:
	print('none')
