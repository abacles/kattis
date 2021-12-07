from collections import deque

def file_id(f):
	global ni
	if f not in f2i:
		f2i[f] = ni
		i2f.append(f)
		ni += 1
	return f2i[f]

def bfs(v):
	q = deque([v])
	visited = [False] * n
	ndeps[v] = 0
	while len(q) > 0:
		v = q.popleft()
		for w in deps[v]:
			if not visited[w]:
				q.append(w)
				visited[w] = True
			ndeps[w] = ndeps[w] + 1 if ndeps[w] != -1 else 1

def topsort(v):
	q = deque([v])
	while len(q) > 0:
		v = q.popleft()
		print(i2f[v])
		for w in deps[v]:
			if ndeps[w] > 0:
				ndeps[w] -= 1
				if ndeps[w] == 0:
					q.append(w)

n = int(input())
f2i = {}
i2f = []
ni = 0
deps = [[] for _ in range(n)]
for i in range(n):
	files = input().split()
	thisf = files[0][:-1]
	x = file_id(thisf)
	for j in range(1, len(files)):
		y = file_id(files[j])
		deps[y].append(x)

changed = f2i[input()]
ndeps = [-1] * n
bfs(changed)
topsort(changed)
