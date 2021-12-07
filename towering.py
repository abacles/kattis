def arrange(a, s):
	for i in range(6):
		for j in range(i+1, 6):
			for k in range(j+1, 6):
				if a[i] + a[j] + a[k] == s:
					return [i, j, k]

everything = [int(_) for _ in input().split()]
blocks = everything[:-2]
left = arrange(blocks, everything[-2])
right = [i for i in range(6) if i not in left]
left = sorted([blocks[i] for i in left], reverse = True)
right = sorted([blocks[i] for i in right], reverse = True)
print(' '.join(str(x) for x in left+right))
