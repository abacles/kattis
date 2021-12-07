a, b = [int(_) for _ in input().split()]
tot = 0
for i in range(b+1):
    tot += 2**i
if tot >= a:
    print('yes')
else:
    print('no')
    
