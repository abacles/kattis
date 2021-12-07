def pospush(k, i):
    if k in pos:
        pos[k].add(i)
    else:
        pos[k] = {i}

ncards = int(input())
nturns = int(input())
available = ncards
pos = {}
done = set()
for i in range(nturns):
    guess = input().split()
    pospush(guess[-1], int(guess[1]))
    pospush(guess[-2], int(guess[0]))
    if guess[-1] == guess[-2]:
        available -= 2
        done.add(guess[-1])
half = 0
full = 0
for card in pos:
    if card not in done:
        if len(pos[card]) == 2:
            full += 1
            available -= 2
        else:
            half += 1
if available == 2*half:
    print(full+half)
elif available == 2:
    print(full+1)
else:
    print(full)
