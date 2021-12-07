import sys, math

for line in sys.stdin:
    r, x, y = [float(_) for _ in line.split()]
    dist = math.hypot(x, y)
    if dist > r:
        print('miss')
    else:
        theta = math.acos(dist/r)
        area = r * r * (math.pi-theta) + dist * math.sin(theta) * r
        print(area, math.pi*r*r - area)
