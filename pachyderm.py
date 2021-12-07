while True:
    n = int(input())
    if n == 0:
        break
    boxes = [input().split() for i in range(n)]
    for i in range(n):
        for j in range(4):
            boxes[i][j] = float(boxes[i][j])
    m = int(input())
    for i in range(m):
        x, y, size = input().split()
        x = float(x)
        y = float(y)
        for j in range(n):
            if boxes[j][0] <= x <= boxes[j][2] and boxes[j][1] <= y <= boxes[j][3]:
                print(size, 'correct' if size == boxes[j][4] else boxes[j][4])
                break
        else:
            print(size, 'floor')
    print()
