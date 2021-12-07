for c in range(int(input())):
    c, r = [int(_) for _ in input().split()]
    weights = [[int(_) for _ in input().split()] for i in range(r)]
    rsum = sum(weights[0])
    rpsum = [rsum]
    for i in range(1, r):
        rsum += sum(weights[i])
        rpsum.append(rsum)
    csum = sum([weights[_][0] for _ in range(r)])
    cpsum = [csum]
    for i in range(1, c):
        csum += sum([weights[_][i] for _ in range(r)])
        cpsum.append(csum)
    cost = 0
    for i in range(1, r):
        cost += i * (rpsum[i]-rpsum[i-1])
    rmincost = cost
    rmin = 0
    for i in range(1, r):
        partnext = rsum - rpsum[i-1]
        cost = cost - partnext + rpsum[i-1]
        if cost < rmincost:
            rmincost = cost
            rmin = i
    cost = 0
    for i in range(1, c):
        cost += i * (cpsum[i]-cpsum[i-1])
    cmincost = cost
    cmin = 0
    for i in range(1, c):
        partnext = csum - cpsum[i-1]
        cost = cost - partnext + cpsum[i-1]
        if cost < cmincost:
            cmincost = cost
            cmin = i
    print(rmincost + cmincost, 'blocks')
