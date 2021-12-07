n = int(input())
infections = [[0] * 3 for i in range(2)]
groupsize = [0, 0]
for i in range(n):
    subj = [1 if x == 'Y' else 0 for x in input()]
    groupsize[subj[0]] += 1
    for j in range(3):
        infections[subj[0]][j] += subj[j+1]
        
for i in range(3):
    pcb = infections[0][i] / groupsize[0]
    vax = infections[1][i] / groupsize[1]
    if vax >= pcb:
        print('Not Effective')
    else:
        eff = (pcb - vax) / pcb
        print(eff * 100)
