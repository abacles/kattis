while True:
    segs = int(input())
    if segs == -1:
        break
    tot,prev = 0,0
    for i in range(segs):
        seg = [int(_) for _ in input().split()]
        tot += seg[0] * (seg[1] - prev)
        prev = seg[1]
    print(tot,'miles')
