while True:
    n = int(input())
    if n < 0:
        break
    adj = [[_ == '1' for _ in input().split()] for i in range(n)]
    weak = []
    for i in range(n):
        strong = False
        for j in range(n):
            if adj[i][j]:
                for k in range(j+1, n):
                    if adj[i][k] and adj[j][k]:
                        strong = True
                        break
            if strong:
                break
        if not strong:
            weak.append(i)
    print(' '.join([str(_) for _ in weak]))
