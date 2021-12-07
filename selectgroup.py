import sys

def ev(ex):
    if ex[0] == 'union':
        ex,l = ev(ex[1:])
        ex,r = ev(ex)
        return ex,l | r
    elif ex[0] == 'intersection':
        ex,l = ev(ex[1:])
        ex,r = ev(ex)
        return ex,l & r
    elif ex[0] == 'difference':
        ex,l = ev(ex[1:])
        ex,r = ev(ex)
        return ex,l - r
    else:
        return ex[1:],groups[ex[0]]

groups = {}

everything = sys.stdin.read().split('\n')

for line in everything:
    if not line:
        break
    exp = line.split()
    if exp[0] == 'group':
        groups[exp[1]] = set(exp[3:])
    else:
        if exp[0] == 'union':
            print(' '.join(sorted(ev(exp)[1])))
        elif exp[0] == 'intersection':
            print(' '.join(sorted(ev(exp)[1])))
        else:
            print(' '.join(sorted(ev(exp)[1])))
