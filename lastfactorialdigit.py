for c in range(int(input())):
    n = int(input())
    fac = 1
    for x in range(n, 1, -1):
        fac = (fac * x) % 10
    print(fac)
