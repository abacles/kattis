while True:
    s = input()
    if s == '0':
        break
    p = [float(_) for _ in s.split()]
    d = (abs(p[0]-p[2])**p[4] + abs(p[1]-p[3])**p[4]) ** (1/p[4])
    print(d)
