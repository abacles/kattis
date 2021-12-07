import math

for t in range(int(input())):
    m = int(input())
    x = y = 0
    facing = math.pi/2
    for i in range(m):
        theta, dist = [float(_) for _ in input().split()]
        facing += math.radians(theta)
        x += dist * math.cos(facing)
        y += dist * math.sin(facing)
    print(x, y)
