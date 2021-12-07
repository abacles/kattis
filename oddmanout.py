for c in range(int(input())):
    alone = set()
    input()
    people = [int(_) for _ in input().split()]
    for p in people:
        if p in alone:
            alone.remove(p)
        else:
            alone.add(p)
    print('Case #' + str(c+1) + ': ' + str(list(alone)[0]))
