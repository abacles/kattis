import math

ams = input().split()
npies, nrings, rad = int(ams[0]), int(ams[1]), float(ams[2])
pos = [int(_) for _ in input().split()]

s = (pos[1] + pos[3]) * rad / nrings
for r in range(1, min(pos[1],pos[3])+1):
    dist = (abs(pos[2] - pos[0]) / npies) * r/nrings * rad * math.pi + \
           (abs(pos[1] - r) + abs(pos[3] - r)) * rad / nrings
    s = min(s, dist)
    
print(s)
