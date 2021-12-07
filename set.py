def distinct(a, b, c):
    return a != b and b != c and a != c

cards = []
for i in range(4): cards.extend(input().split())

found = False

for i in range(12):
    for j in range(i+1, 12):
        for k in range(j+1, 12):
            for s in range(4):
                if not (cards[i][s] == cards[j][s] == cards[k][s] or
                        distinct(cards[i][s], cards[j][s], cards[k][s])):
                    break
            else:
                print(i+1, j+1, k+1)
                found = True
if not found:
    print('no sets')
