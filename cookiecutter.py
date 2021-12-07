import math

def polyarea(corners):
    n = len(corners)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

vcount = int(input())
vertices = []
for i in range(vcount):
    vertices.append([float(x) for x in input().split()])
newarea = int(input())

minx = min(vertices,key = lambda x: x[0])[0]
miny = min(vertices,key = lambda x: x[1])[1]
for i in range(vcount):
    vertices[i][0] += 0-minx
    vertices[i][1] += 0-miny

oldarea = polyarea(vertices)
scale = math.sqrt(newarea / oldarea)

for i in range(vcount):
    print(str(vertices[i][0]*scale) + ' ' + str(vertices[i][1]*scale))
