n = int(input())
plays = [int(_) for _ in input().split()]
pcount = 0
pos = 20
gain = 0
for i in range(n):
    pos += plays[i]
    gain += plays[i]
    pcount += 1
    if pos >= 100 or pos <= 0:
        print('Touchdown' if pos >= 100 else 'Safety')
        break
    elif gain >= 10:
        pcount = 0
        gain = 0
    elif pcount == 4:
        print('Nothing')
        break
else:
    print('Nothing')
