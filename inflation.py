n = int(input())
canisters = sorted([int(_) for _ in input().split()])
minfrac = 1
for i in range(n):
    frac = canisters[i] / (i+1)
    if frac > 1:
        print('impossible')
        quit()
    if frac < minfrac:
        minfrac = frac
print(minfrac)
