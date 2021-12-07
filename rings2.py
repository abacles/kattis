l,w=[int(x) for x in input().split()]
tree=[]
for i in range(l):
  tree.append(input())
inf=101
rings=[x[:] for x in [[inf]*w]*l]
row=range(l)
col=range(w)
for c in range(2):
  for i in row:
    for j in col:
      if tree [i][j]=='.':
        rings [i][j]=0
      else:
        cmin=inf
        if i>0:
          cmin=min(cmin,rings [i-1][j])
        else:
          cmin=0
        if i<l-1:
          cmin=min(cmin,rings [i+1][j])
        else:
          cmin=0
        if j>0:
          cmin=min(cmin,rings [i][j-1])
        else:
          cmin=0
        if j<w-1:
          cmin=min(cmin,rings [i][j+1])
        else:
          cmin=0
        rings [i][j]=cmin+1
  row=range(l-1,-1,-1)
  col=range(w-1,-1,-1)
rcount=max([max(x) for x in rings])
for i in range(l):
    for j in range(w):
        print('.',end='')
        if rcount<10:
            if rings [i][j]==0:
                print('.',end='')
            else:
                print(rings [i][j],end='')
        else:
            if rings [i][j]==0:
                print('..',end='')
            elif rings [i][j]<10:
                print('.'+str(rings [i][j]),end='')
            else:
                print(rings [i][j],end='')
    print()
