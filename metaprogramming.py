import sys

everything = sys.stdin.read().strip().split('\n')

vartable = {}
for line in everything:
    parts = line.split()
    if parts[0][0] == 'd':
        vartable[parts[2]] = int(parts[1])
    elif parts[0][0] == 'e':
        if parts[1] not in vartable or parts[3] not in vartable:
            print('undefined')
        else:
            a = vartable[parts[1]]; b = vartable[parts[3]]
            if parts[2] == '<':
                comp = a < b
            elif parts[2] == '=':
                comp = a == b
            elif parts[2] == '>':
                comp = a > b
            print(str(comp).lower())
