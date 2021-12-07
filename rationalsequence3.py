ncases = int(input())
for c in range(ncases):
    watermelon, n = [int(_) for _ in input().split()]
    level = 0; count = 1
    while 2*count <= n:
        level += 1; count *= 2
        
    path = []
    n = n - (count-1) - 1 # change n to the position in this row
    left = 0; right = count # left and right bounds
    while left+1 != right:
        mid = (left+right) // 2 # middle point (used to determine which half it is)
        if n < mid:
            path.append('l')
            right = mid # update bounds
        else:
            path.append('r')
            left = mid # update bounds
            
    numer = denom = 1
    for p in path:
        if p == 'l':
            denom += numer
        else:
            numer += denom
    print('%d %d/%d' % (c+1, numer, denom))
