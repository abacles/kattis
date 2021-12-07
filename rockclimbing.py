def improv(old):
    while True:
        new = [row[:] for row in old]
        for i in range(0,rcount+2):
            for j in range(ccount):
                for x in [-1,1]:
                    if 0 <= j+x < ccount:
                        new[i][j] = max(0,min(new[i][j],old[i][j+x]+cliff[i][j]))
                for y in [-1,1]:
                    if 0<= i+y < rcount+2:
                        new[i][j] = max(0,min(new[i][j],old[i+y][j]+cliff[i][j]))
        if old == new:
            return new
        old = [row[:] for row in new]

rcount,ccount = [int(x) for x in input().split()]
input()
cliff = [[0]*ccount]
for i in range(rcount):
    cliff.append([int(x) for x in input().split()])
input()
cliff.append([0]*ccount)

energy = [[100000 for i in range(ccount)] for j in range(rcount+2)]
for i in range(ccount):
    energy[0][i] = 0
    
energy = improv(energy)
print(min(energy[rcount+1]))
