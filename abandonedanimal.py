def nextcombo(curr):
    newcombo = combo.copy()
    for s in range(len(template)):
        for i in range(len(template[s])):
            if template[s][i] > curr[s]:
                newcombo[s] = template[s][i]
                return newcombo
        newcombo[s] = template[s][0]
    return None

smcount = int(input())
icount = int(input())
canbefound = {}
for i in range(icount):
    item = input().split()
    if item[1] in canbefound:
        canbefound[item[1]].append(int(item[0]))
    else:
        canbefound[item[1]] = [int(item[0])]
bcount = int(input())
shoplist = []
for i in range(bcount):
    shoplist.append(input())

template = []
key = {}
i = 0
for item in canbefound.keys():
    key[item] = i
    template.append(canbefound[item])
    i += 1
    
combo = []
# initialize by choosing the first item for each slot
for slot in template:
    combo.append(slot[0])

status = None
while combo != None:
    order = []
    for item in shoplist:
        order.append(combo[key[item]])
    success = True
    for i in range(1,len(order)):
        if order[i] < order[i-1]:
            success = False
            break
    if success and status != None:
        status = 'ambiguous'
        break
    if success:
        status = 'unique'
    combo = nextcombo(combo)
    
if status == None:
    status = 'impossible'
print(status)
