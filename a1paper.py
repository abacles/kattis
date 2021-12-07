def use(available,needsize,need,start):
  if available.get(start)==None:
    return [False]
  need-=available [start]
  if need<=0:
    return [need+available [start]]
  else:
    if need==1:
      smaller=use(available,needsize+1,2,start+1)
    else:
      smaller=use(available,needsize,need*2,start+1)
    if smaller==[False]:
      return [False]
    if available [start]>0:
      return [available [start]]+smaller
    else:
      return [False]+smaller


smallest=int(input())
papers={}
buff=input().split()
for size in range(2,smallest+1):
  papers [size]=int(buff [size-2])
used=use(papers,1,2,2)
# print(used)
if used==[False]:
  print('impossible')
else:
  length=2**(-3/4)
  width=2**(-5/4)
  tape=0
  unoccupied=1
  for sizeused in used:
    tape+=unoccupied*length
    if sizeused!=False:
      unoccupied=unoccupied*2-sizeused
    else:
      unoccupied*=2
    prevl=length
    length=width
    width=prevl/2
  print(tape)
