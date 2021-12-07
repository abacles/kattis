placed = set()
count = 0
for i in range(int(input())):
    univ,team = input().split()
    if not univ in placed and count < 12:
        print(univ,team)
        placed.add(univ)
        count += 1
