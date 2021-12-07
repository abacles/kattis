x,y = [int(_) for _ in input().split()]
shieldcount = int(input())
shields = []
for s in range(shieldcount):
    shield = input().split()
    shield[0],shield[1],shield[2] = int(shield[0]),int(shield[1]),float(shield[2])
    shields.append(shield)
shields.sort(key=lambda x: x[0])
prev,norm,slow = 0,0,0 # norm in minutes
for s in shields:
    norm += s[0] - prev
    slow += (s[1]-s[0]) * s[2]
    prev = s[1]
norm += y - prev
print(x / (norm + slow))
