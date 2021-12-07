minions=int(input())
temprange=[]
for i in range(minions):
    temprange.append([int(temp) for temp in input().split()])
temprange=sorted(temprange,key=lambda x: x [1])
rooms=[]
for i in range(minions):
    if len(rooms)>0:
        last=rooms [len(rooms)-1]
        if temprange [i][0]<=last and last<=temprange [i][1]:
            continue
    rooms.append(temprange [i][1])
print(len(rooms))
