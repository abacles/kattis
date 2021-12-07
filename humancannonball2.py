import math

for _ in range(int(input())):
    v, t, x, hl, hh = [float(_) for _ in input().split()]
    time = x / v / math.cos(math.radians(t))
    y = v * time * math.sin(math.radians(t)) - 0.5 * 9.81 * time ** 2
    if hl + 1 <= y <= hh - 1:
        print('Safe')
    else:
        print('Not Safe')
