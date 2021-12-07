import math

while True:
    r, m, c = [float(_) for _ in input().split()]
    if r == m == c == 0:
        break
    print(math.pi*r*r, (4*r*r) * c / m)
