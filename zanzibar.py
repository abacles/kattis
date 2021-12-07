for _ in range(int(input())):
    pop = [int(_) for _ in input().split()]
    imported = 0
    for i in range(1, len(pop)):
        imported += max(0, pop[i] - 2 * pop[i-1])
    print(imported)
