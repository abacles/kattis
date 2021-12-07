while(1):
    g = int(input())
    if g != 0:
        pts = []
        line = []
        ollie = 0
        stan = 0
        for i in range(g):
            h = [int(_) for _ in input().split()]
            pts.append(h)
            if i == int((g / 2) - 0.5):
                line = h
        for i in pts:
            x = i[0] - line[0]
            y = i[1] - line[1]
            if (x > 0 and y > 0) or (x < 0 and y < 0):
                stan += 1
            elif(x > 0 and y < 0) or (x < 0 and y > 0):
                ollie += 1
        print(stan, ollie)
    else:
        break
