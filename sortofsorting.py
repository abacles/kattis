while True:
    n = int(input())
    if not n:
        break
    names = sorted([input() for _ in range(n)], key = lambda x: x[:2])
    for n in names:
        print(n)
    print()
