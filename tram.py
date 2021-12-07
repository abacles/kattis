n = int(input())
print(sum(v[1] - v[0] for v in [[int(_) for _ in input().split()] for i in range(n)]) / n)
