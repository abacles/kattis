import math

t, n = input().split()
t = float(t); n = int(n)
w = sorted([int(_) for _ in input().split()])

cuts = 500
for i in range(n):
    j = 1
    while j * (n-i) < cuts:
        maxpiece = w[i] / j
        c = 0
        for k in range(n):
            tmp = math.ceil(w[k] / maxpiece)
            if w[k] / tmp < maxpiece * t:
                break
            c += tmp - 1
        else:
            cuts = min(cuts, c)
        j += 1
print(cuts)
