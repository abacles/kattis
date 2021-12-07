def pfac(n):
    for i in range(2,1000):
        if n % i == 0:
            return i,n/i

cases = int(input())
for i in range(cases):
    n,e = [int(x) for x in input().split()]
    f1,f2 = pfac(n)
    totient = (f1-1) * (f2-1)
    d = 2
    while d*e % totient != 1:
        d += 1
    print(d)
