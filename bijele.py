need,have = [1,1,2,2,2,8],[int(_) for _ in input().split()]
print(' '.join([str(need[i]-have[i]) for i in range(6)]))
