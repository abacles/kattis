import heapq

nppl, locktime = [int(_) for _ in input().split()]
logons = sorted([[int(_) for _ in input().split()] for i in range(nppl)])

workstations = []
unlocks = 0
for i in range(nppl):
	while len(workstations) > 0 and workstations[0]+locktime < logons[i][0]:
		heapq.heappop(workstations)
	if len(workstations) > 0 and workstations[0] <= logons[i][0]:
		heapq.heapreplace(workstations, logons[i][0]+logons[i][1])
	else:
		heapq.heappush(workstations, logons[i][0]+logons[i][1])
		unlocks += 1
print(nppl - unlocks)
