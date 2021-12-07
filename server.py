n, t = [int(_) for _ in input().split()]
tasks = [int(_) for _ in input().split()]
i = 0
while i < n:
	if t < tasks[i]:
		break
	t -= tasks[i]
	i += 1
print(i)
