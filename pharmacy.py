import heapq

def next_task(q):
	return q[-1][0] if q else 10e20

nq, nworkers = [int(_) for _ in input().split()]
sq = []
rq = []
for i in range(nq):
	rtime, rtype, ctime = input().split()
	if rtype == 'S':
		sq.append((int(rtime), int(ctime)))
	else:
		rq.append((int(rtime), int(ctime)))
sq.sort(reverse = True)
rq.sort(reverse = True)

workers = [0] * nworkers
stot = rtot = sc = rc = 0
clock = 0
while len(sq) + len(rq) > 0:
	clock = max(workers[0], min(next_task(sq), next_task(rq)))
	if clock >= next_task(sq):
		heapq.heapreplace(workers, clock + sq[-1][1])
		stot += (clock + sq[-1][1]) - sq[-1][0]
		sc += 1
		sq.pop()
	elif clock >= next_task(rq):
		heapq.heapreplace(workers, clock + rq[-1][1])
		rtot += (clock + rq[-1][1]) - rq[-1][0]
		rc += 1
		rq.pop()
	else: print("we're in trouble :(");

print(stot/sc if sc else 0, rtot/rc if rc else 0)
