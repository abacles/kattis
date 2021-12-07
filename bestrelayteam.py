n = int(input())
candidates = [None] * n
for i in range(n):
	name, *time = input().split()
	candidates[i] = (name, float(time[0]), float(time[1]))
mintime = 100
stimes = sorted(((i, candidates[i][-1]) for i in range(n)), key = lambda x: x[1])
cteam = [0] * 3
for i in range(n):
	time = candidates[i][1]
	for j in range(3):
		if stimes[j][0] == i:
			time += stimes[3][1]
			cteam[j] = stimes[3][0]
		else:
			time += stimes[j][1]
			cteam[j] = stimes[j][0]
	if time < mintime:
		mintime = time
		team = [i] + cteam
print(mintime)
for p in team:
	print(candidates[p][0])
