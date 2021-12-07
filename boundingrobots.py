while True:
    w, l = [int(_) for _ in input().split()]
    if w == l == 0:
        break
    n = int(input())
    robx = roby = accx = accy = 0
    for i in range(n):
        direction, step = input().split()
        step = int(step)
        if direction == 'u':
            roby += step
            accy += step
        elif direction == 'd':
            roby -= step
            accy -= step
        elif direction == 'l':
            robx -= step
            accx -= step
        elif direction == 'r':
            robx += step
            accx += step
        accx = max(0, min(accx, w-1))
        accy = max(0, min(accy, l-1))
    print('Robot thinks', robx, roby)
    print('Actually at', accx, accy)
    print()
