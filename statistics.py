import sys

inf=sys.stdin.read()
i=1
for line in inf.split('\n'):
    if line=='':
        break
    numcount=line.split() [0]
    data=[int(x) for x in line.split() [1:]]
    print('Case '+str(i)+': '+str(min(data))+' '+str(max(data))+' '+str(max(data)-min(data)))
    i+=1
