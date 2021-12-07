roomcount,booked=[int(x) for x in input().split()]
available=[x+1 for x in range(roomcount)]
for i in range(booked):
  available.remove(int(input()))
if available==[]:
  print('too late')
else:
  print(available [0])
