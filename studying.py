step = 0.001

def ev(tnum, x):
    return tests[tnum][0] * x**2 + tests[tnum][1] * x + tests[tnum][2]

ntests, ttime = [int(_) for _ in input().split()]
tests = [[float(_) for _ in input().split()] for _ in range(ntests)]
used = [0] * ntests
tot = sum([ev(_, 0) for _ in range(ntests)])
time = 0
while time < ttime:
    best = 0
    for t in range(ntests):
        c = ev(t, used[t] + step) - ev(t, used[t])
        if c > best:
            best = c
            bt = t
    tot += best
    used[bt] += step
    time += step

print(tot / ntests)
