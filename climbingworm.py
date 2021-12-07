climb, fall, pole = [int(_) for _ in input().split()]
h = 0
i = 0
while h < pole:
  h += climb
  if h < pole:
    h -= fall
  i += 1
print(i)
