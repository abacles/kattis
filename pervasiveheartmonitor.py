import sys

for line in sys.stdin:
    stuff = line.split()
    name = []
    s = c = 0
    for thing in stuff:
        if thing[0].isalpha():
            name.append(thing)
        else:
            s += float(thing)
            c += 1
    print(s / c, ' '.join(name))
