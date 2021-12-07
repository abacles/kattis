length = int(input())
notes = input().split()
lraw = 'abcdefgABCDEFG'
lines = {}
for l in lraw:
    lines[l] = set()
pos = 0
for n in notes:
    dur = 1 if len(n) == 1 else int(n[1])
    for i in range(dur):
        lines[n[0]].add(pos)
        pos += 1
    pos += 1
for line in reversed(lraw):
    print(line + ': ', end = '')
    sep = '-' if line in 'FDBgea' else ' '
    for i in range(pos-1):
        if i in lines[line]:
            print('*', end = '')
        else:
            print(sep, end = '')
    print()
