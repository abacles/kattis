hands,trump = input().split()
points = {'A':11,'K':4,'Q':3,'J':2,'T':10,'9':0,'8':0,'7':0}
total = 0
for h in range(4*int(hands)):
    card = input()
    total += points[card[0]]
    if card[1] == trump:
        if card[0] == 'J':
            total += 18
        elif card[0] == '9':
            total += 14
print(total)
