nppl = int(input())
ndays = int(input())
songs = [set() for i in range(nppl)]
for i in range(ndays):
	ppl = [int(_) for _ in input().split()][1:]
	if 1 in ppl:
		for j in range(len(ppl)):
			songs[ppl[j]-1].add(i)
	else:
		allsongs = set()
		for j in range(len(ppl)):
			allsongs |= songs[ppl[j]-1]
		for j in range(len(ppl)):
			songs[ppl[j]-1] = allsongs.copy()

for i in range(nppl):
	if len(songs[i]) == len(songs[0]):
		print(i+1)
