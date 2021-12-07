for t in range(int(input())):
    n = int(input())
    wood = sorted([sum(int(_) for _ in input().split()[1:]) for i in range(n)])
    time = tot = 0
    for x in wood:
        time += x
        tot += time
    print(tot / n)
