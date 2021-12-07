nprobs, fav = [int(_) for _ in input().split()]
solvtime = [int(_) for _ in input().split()]
order = [solvtime[fav]] + sorted([solvtime[i] for i in range(nprobs) if i!=fav])
penalty = time = solvd = 0
for i in range(nprobs):
	time += order[i]
	if time > 300: break;
	penalty += time
	solvd += 1
print(solvd, penalty)
