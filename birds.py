l, d, nbirds = [int(_) for _ in input().split()]
pos = []
for i in range(nbirds):
    pos.append(int(input()))
pos.sort()
pos = [6-d] + pos + [l-6+d]
morebirds = 0
for i in range(len(pos)-1):
    morebirds += max((pos[i+1] - pos[i]) // d - 1, 0)
print(morebirds)
