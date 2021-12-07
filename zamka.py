lo,hi,sod = int(input()),int(input()),int(input())
for n in range(lo,hi+1):
    if sum([int(_) for _ in str(n)]) == sod:
        break
for m in range(hi,lo-1,-1):
    if sum([int(_) for _ in str(m)]) == sod:
        break
print(n)
print(m)
