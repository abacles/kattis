for t in range(int(input())):
    poly = [int(_) for _ in input().split()[1:]]
    a = 0
    for i in range(0, len(poly), 2):
        a += poly[i] * (poly[(i+3)%len(poly)] - poly[(i-1+len(poly))%len(poly)])
    print(a / 2)
