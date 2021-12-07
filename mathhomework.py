b, c, d, totlegs = [int(_) for _ in input().split()]
solvd = False
for i in range(totlegs//b+1):
  for j in range((totlegs-b*i)//c+1):
    for k in range((totlegs-b*i-c*j)//d+1):
      if i*b + j*c + k*d == totlegs:
        print(i, j, k)
        solvd = True
if not solvd:
  print('impossible')
