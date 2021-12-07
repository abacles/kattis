d1, d2 = [int(_) for _ in input().split()]

sums_count = {}
for i in range(1, d1+1):
    for j in range(1, d2+1):
	if i+j in sums_count:
	    sums_count[i+j] += 1
	else:
	    sums_count[i+j] = 1
most_likely = max(sums_count, key = sums_count.get)
for i in sorted(sums_count.keys()):
    if sums_count[i] == sums_count[most_likely]:
        print(i)
