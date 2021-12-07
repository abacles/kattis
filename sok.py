have = [int(_) for _ in input().split()]
need = [int(_) for _ in input().split()]
servings = min(have[_]/need[_] for _ in range(3))
print(' '.join([str(have[_]-need[_]*servings) for _ in range(3)]))
