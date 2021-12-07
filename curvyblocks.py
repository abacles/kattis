import sys, math

def f(w, x):
    return w[0] + w[1]*x + w[2]*(x**2) + w[3]*(x**3)

allin = []
for line in sys.stdin:
    allin.append(line)
    
for i in range(0, len(allin), 2):
    bot = [float(_) for _ in allin[i].split()]
    top = [float(_) for _ in allin[i+1].split()]
    diff = [top[_] - bot[_] for _ in range(4)]
    a = diff[-1] * 3
    b = diff[-2] * 2
    c = diff[-3]
    candidates = [0, 1]
    if a == 0 and b == 0:
        pass
    elif a == 0:
        if 0 <= -c/b <= 1:
            candidates += [-c/b]
    elif b**2-4*a*c >= 0:
        x1 = (-b + math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b**2-4*a*c))/(2*a)
        if 0 <= x1 <= 1:
            candidates += [x1]
        if 0 <= x2 <= 1:
            candidates += [x2]
    candidates = [f(diff, _) for _ in candidates]
    print(max(candidates) - min(candidates))
