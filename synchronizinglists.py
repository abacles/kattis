while True:
    n = int(input())
    if n == 0:
        break
    l1 = [int(input()) for _ in range(n)]
    sl1 = sorted(l1)
    ordering = {sl1[i]: i for i in range(n)}
    sl2 = sorted([int(input()) for _ in range(n)])
    for i in range(n):
        print(sl2[ordering[l1[i]]])
    print()
