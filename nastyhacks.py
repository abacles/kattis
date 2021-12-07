for c in range(int(input())):
    n,y,cost = [int(_) for _ in input().split()]
    if y - n > cost:
        print('advertise')
    elif y - n < cost:
        print('do not advertise')
    else:
        print('does not matter')
