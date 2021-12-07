while True:
    nmirrors = int(input())
    if not nmirrors:
        break
    mirrors = []
    for i in range(nmirrors):
        mirrors.append([int(_) for _ in input().split()])
    npoints = int(input())
    for i in range(npoints):
        x, y = [int(_) for _ in input().split()]
        see = 0
        for m in mirrors:
            if m[0] == m[2]:
                see += int(min(m[1], m[3]) <= y <= max(m[1], m[3]))
            elif m[1] == m[3]:
                see += int(min(m[0], m[2]) <= x <= max(m[0], m[2]))
            else:
                ktop = -(m[2]-m[0]); kbot = (m[3]-m[1])
                if kbot < 0:
                    ktop = -ktop; kbot = -kbot
                p1top = m[1]*kbot + (x-m[0]) * ktop
                p2top = m[3]*kbot + (x-m[2]) * ktop
                see += int(min(p1top, p2top) <= y*kbot <= max(p1top, p2top))
        print(see)
    print()
