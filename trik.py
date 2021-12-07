moves,pos = input(),1
for ch in moves:
    if ch == 'A' and pos != 3:
        pos = 3 - pos
    elif ch == 'B' and pos != 1:
        pos = 5 - pos
    elif ch == 'C' and pos != 2:
        pos = 4 - pos
print(pos)
