import sys

lines = [_.strip() for _ in sys.stdin]
read = 0

while read < len(lines):
    domain = set((lines[read].split())[1:])
    codomain = set((lines[read+1].split())[1:])
    n = int(lines[read+2])
    function = injective = True
    read += 3
    for i in range(read, read+n):
        a, b = lines[i].split(' -> ')
        if a not in domain:
            function = False
        if b not in codomain:
            injective = False
        domain.discard(a)
        codomain.discard(b)
    surgective = len(codomain) == 0
    read += n
    if not function:
        print('not a function')
    elif injective and surgective:
        print('bijective')
    elif injective:
        print('injective')
    elif surgective:
        print('surjective')
    else:
        print('neither injective nor surjective')
