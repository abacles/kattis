c = 1
while True:
    na = int(input())
    if not na:
        break
    ani = [(input().split()[-1]).lower() for _ in range(na)]
    anilist = {}
    for a in ani:
        anilist[a] = anilist.get(a, 0) + 1
    print('List %d:' % c)
    for a in sorted(anilist.keys()):
        print(a, '|', anilist[a])
    c += 1
