n = int(input())
paths = [int(_) for _ in input().split()]
a = int(input())
queries = [int(_) for _ in input().split()]

lead_to = [paths[i] if paths[i] >= 0 else i for i in range(n)]
steps = [0] * n
for i in range(n):
	j = i
	while lead_to[j] != j:
		steps[i] += steps[j] if lead_to[j] != paths[j] else 1
		j = lead_to[j]
	lead_to[i] = j

is_pipe = [True] * n
for i in range(n):
	if paths[i] == -1:
		is_pipe[i] = False
	else:
		is_pipe[paths[i]] = False

best_pipe = [-1] * n
for i in range(n):
	if is_pipe[i] and (best_pipe[lead_to[i]] == -1 or steps[i] < steps[best_pipe[lead_to[i]]]):
		best_pipe[lead_to[i]] = i

for q in queries:
	print(best_pipe[lead_to[q]])
