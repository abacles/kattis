nparts, ndays = [int(_) for _ in input().split()]
parts = set()
for i in range(ndays):
    parts.add(input())
    if len(parts) >= nparts:
        break
if len(parts) < nparts:
    print('paradox avoided')
else:
    print(i + 1)
