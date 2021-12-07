def mpart(b,n,maxpower):
    partitions = 0
    if maxpower <= 0:
        return 1
    for i in range(1,maxpower+1):
        k = b**i
        if k > n:
            break
        j = 1
        while k*j <= n:
            if (n-k*j,i-1) in lib:
                partitions += lib[(n-k*j)*100 + i-1]
            else:
                partitions += mpart(b,n-k*j,i-1)
            j += 1
    lib[n*100 + maxpower] = partitions + 1
    return partitions + 1

cases = int(input())
lib = {}
for i in range(cases):
    lib.clear()
    foo,base,n = [int(x) for x in input().split()]
    print(str(i+1) + ' ' + str(mpartfast(base,n)))
