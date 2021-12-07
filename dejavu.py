import sys

everything = [int(_) for _ in sys.stdin.read().split()]

npoints = everything[0]
xcount = {}; ycount = {};
for i in range(npoints):
    x = everything[1+2*i]; y = everything[2+2*i]
    xcount[x] = xcount.get(x, 0) + 1
    ycount[y] = ycount.get(y, 0) + 1

tri = 0
for i in range(npoints):
    x = everything[1+2*i]; y = everything[2+2*i]
    tri += (xcount[x]-1) * (ycount[y]-1)

print(tri)
