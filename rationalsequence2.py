def uptrace(n, d):
    p = []
    while not (n == d == 1):
        if n < d:
            p.append('L')
            d -= n
        else:
            p.append('R')
            n -= d
    return list(reversed(p))

def pos(path):
    bounds = [0, 2**len(path)]
    for i in range(len(path)):
        if path[i] == 'L':
            bounds[1] -= (bounds[1]-bounds[0]) // 2
        else:
            bounds[0] += (bounds[1]-bounds[0]) // 2
    return bounds[0] + 2**len(path)

for c in range(int(input())):
    foo, frac = input().split()
    numer, denom = [int(_) for _ in frac.split('/')]
    path = uptrace(numer, denom)
    print(c+1, pos(path))
