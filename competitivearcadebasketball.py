nppl, goal, m = [int(_) for _ in input().split()]
scoreboard = {input(): 0 for i in range(nppl)}
winner = False
for i in range(m):
  point = input().split()
  scoreboard[point[0]] += int(point[1])
  if scoreboard[point[0]] >= goal and scoreboard[point[0]] - int(point[1]) < goal:
    print(point[0], 'wins!')
    winner = True
if not winner:
  print('No winner!')
