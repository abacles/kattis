import math

nbridges, nknights, grpsize = [int(_) for _ in input().split()]

print(math.ceil((nbridges - 1) / (nknights // grpsize)))
