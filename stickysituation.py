def tri():
    for i in range(0, nsticks - 2):
        if sticks[i] + sticks[i+1] > sticks[i+2]:
            return True
    return False

nsticks = int(input())
sticks = sorted([int(_) for _ in input().split()])

if(tri()):
    print('possible')
else:
    print('impossible')
