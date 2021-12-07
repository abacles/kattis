n, x = [int(_) for _ in input().split()]
items = sorted([int(_) for _ in input().split()])
i = 1
while i < n:
    if items[i-1] + items[i] > x:
        break
    i += 1
print(i)
