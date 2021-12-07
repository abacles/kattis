import math

for _ in range(int(input())):
    D, d, s = [float(_) for _ in input().split()]
    c = 0.5 * (D - d)
    a = 0.5 * (d + s)
    print(math.floor(math.pi / (math.asin(a/c))))
