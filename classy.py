hier = {'upper':1,'middle':0,'lower':-1}

for c in range(int(input())):
    fam = []
    for p in range(int(input())):
        person = input().split()
        cl = person[1].split('-')
        scale,cscore = 1,0
        for h in reversed(cl):
            cscore += scale * hier[h]
            scale /= 4
        fam.append((person[0][:-1],cscore))
    fam.sort(key=lambda x: x[0])
    fam.sort(reverse=True,key=lambda x: x[1])
    for p in fam:
        print(p[0])
    print('='*30)
