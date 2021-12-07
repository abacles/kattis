w, p = [int(_) for _ in input().split()]
tmp = [int(_) for _ in input().split()]
l = [False] * w + [True]
for x in tmp:
	l[x] = True
l[0] = True

valid_widths = []
for i in range(1, w+1):
	for j in range(0, w-i+1):
		if l[j] and l[j+i]:
			valid_widths.append(i)
			break
print(' '.join([str(_) for _ in valid_widths]))
