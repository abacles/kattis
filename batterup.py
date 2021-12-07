foo,data = int(input()),[int(_) for _ in input().split()]
print(sum([d if d > -1 else 0 for d in data]) / (foo-data.count(-1)))
