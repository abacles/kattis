while True:
    n, m = [int(_) for _ in input().split()]
    if n == m == 0: break;
    best = -1
    for i in range(n):
        a, b = [int(_) for _ in input().split()]
        if a <= m and (best == -1 or b / a < best or (b / a == best and 
                                                      a > ba)):
            best = b / a
            ba, bb = a, b
    if best == -1:
        print('No suitable tickets offered')
    else:
        print('Buy %d tickets for $%d' % (ba, bb))
