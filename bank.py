n, t = [int(_) for _ in input().split()]
ppl = [[int(_) for _ in input().split()] for i in range(n)]

ppl.sort(key = lambda x: (-x[0], x[1]))

money = 0
busy = [False] * t
for i in range(n):
    for j in range(ppl[i][1], -1, -1):
        if not busy[j]:
            money += ppl[i][0]
            busy[j] = True
            break
print(money)
