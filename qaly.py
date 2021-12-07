n = int(input())
print(sum([(lambda x: x[0]*x[1])([float(_) for _ in input().split()]) for i in range(n)]))
