for _ in range(int(input())):
    length, ants = [int(_) for _ in input().split()]
    a = []
    earliest = 0
    latest = 0
    while len(a) < ants:
        a.extend([int(_) for _ in input().split()])
    for ant in a:
        if length - ant > 0 + ant:
            if length - ant > latest:
                latest = length - ant
            if 0 + ant > earliest:
                earliest = 0 + ant
        else:
            if length - ant > earliest:
                earliest = length - ant
            if 0 + ant > latest:
                latest = 0 + ant
    print(earliest, latest)
