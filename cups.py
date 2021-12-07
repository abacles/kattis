y = []
for _ in range(int(input())):
    x = input().split()
    if (x[0][0]).isalpha():
        rad = int(x[1])
        color = x[0]
    else:
        rad = int(x[0]) / 2
        color = x[1]
    y.append([rad, color])
y.sort(key = lambda x: x[0])
for i in y:
    print(i[1])
