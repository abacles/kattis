tc=int(input())
for c in range(tc):
  trips=int(input())
  distinct=0
  all=[]
  for t in range(trips):
    city=input()
    if not city in all:
      distinct+=1
      all.append(city)
  print(distinct)
