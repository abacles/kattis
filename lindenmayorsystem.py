rules,itr = [int(x) for x in input().split()]
rnew = {}
for i in range(rules):
    rawrule = input()
    rnew[rawrule.split(' -> ')[0]] = rawrule.split(' -> ')[1]
seq = input()

for i in range(itr):
    newseq = []
    for char in seq:
        newseq.append(rnew.get(char,char))
    seq = ''.join(newseq)

print(seq)
