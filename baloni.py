nballoons = int(input())
heights = [int(_) for _ in input().split()]
tails = [0] * 1000001
shots = 0
for h in heights:
	if tails[h] > 0:
		tails[h] -= 1
		tails[h-1] += 1	
	else:
		tails[h-1] += 1
		shots += 1
print(shots)
