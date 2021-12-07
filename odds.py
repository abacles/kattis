import itertools

def mia(a, b, c, d):
    p1 = 10*max(a, b) + min(a, b); p2 = 10*max(c, d) + min(c, d)
    if p1 == 21:
        p1 = 999
    if p2 == 21:
        p2 = 999
    if p1 % 11 == 0:
        p1 *= 10
    if p2 % 11 == 0:
        p2 *= 10
    return 1 if p1 > p2 else 0

def simplify(n, d):
    i = 2
    lim = n
    while i <= lim:
        if not n % i and not d % i:
            n //= i; d //= i
        else:
            i += 1
    if d == 1:
        return str(n)
    if n == 0:
        return '0'
    return '%d/%d' % (n, d)

while True:
    game = input().split()
    if game[0] == game[1] == game[2] == game[3] == '0':
        break
    for i in range(4):
        if game[i] == '*':
            game[i] = list(range(1, 7))
        else:
            game[i] = [int(game[i])]
    wins = total = 0
    for g in itertools.product(*game):
        wins += mia(*g)
        total += 1
    print(simplify(wins, total))
