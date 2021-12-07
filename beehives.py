import math

while True:
    d, n = [float(_) for _ in input().split()]
    n = int(n)
    if d == 0.0 and not n:
        break
    hives = [[float(_) for _ in input().split()] for i in range(n)]
    sour = 0
    for i in range(n):
        for j in range(n):
            if i != j and math.sqrt((hives[i][0]-hives[j][0])**2 + 
                                    (hives[i][1]-hives[j][1])**2) <= d:
                sour += 1
                break
    print('%d sour, %d sweet' % (sour, n-sour))
