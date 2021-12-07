best = (-1,0)
for i in range(5):
    score = sum([int(_) for _ in input().split()])
    if score > best[1]:
        best = (i+1,score)
print(best[0],best[1])
