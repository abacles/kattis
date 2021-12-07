while True:
    a, b, c, d = [int(_) for _ in input().split()]
    if not a and not b and not c and not d:
        break
    p1 = 10*max(a, b) + min(a, b); p2 = 10*max(c, d) + min(c, d)
    if p1 == 21:
        p1 = 999
    if p2 == 21:
        p2 = 999
    if p1 % 11 == 0:
        p1 *= 10
    if p2 % 11 == 0:
        p2 *= 10
    if p1 > p2:
        print('Player 1 wins.')
    elif p2 > p1:
        print('Player 2 wins.')
    else:
        print('Tie.')
