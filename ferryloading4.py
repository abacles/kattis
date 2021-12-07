def load(cap, cars, i):
    loaded = 0
    while i < len(cars) and loaded + cars[i] <= cap:
        loaded += cars[i]
        i += 1
    return i

for c in range(int(input())):
    flen, ncars = [int(_) for _ in input().split()]
    left, right = [], []
    for i in range(ncars):
        car = input().split()
        if car[1][0] == 'l':
            left.append(int(car[0]))
        else:
            right.append(int(car[0]))
    li, ri, lpos, ferry = 0, 0, True, 0
    while li < len(left) or ri < len(right):
        if lpos:
            li = load(flen * 100, left, li)
        else:
            ri = load(flen * 100, right, ri)
        ferry += 1
        lpos = not lpos
    print(ferry)
