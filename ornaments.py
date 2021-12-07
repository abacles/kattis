import math

while True:
    r, h, s = [int(_) for _ in input().split()]
    if not r and not h and not s:
        break
    hang = math.sqrt(h**2 - r**2)
    theta = 2 * math.atan(hang / r)
    print('%.2f' % ((2*hang + (2*math.pi - theta)*r) * (1+s/100)))
