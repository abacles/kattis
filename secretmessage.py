import math
for c in range(int(input())):
    orig = input()
    size = math.ceil(math.sqrt(len(orig)))
    orig += '*' * (size**2 - len(orig))
    matrix = []
    for i in range(size):
        matrix.append(orig[size*i:size*(i+1)])
    for i in range(size):
        for j in range(size-1,-1,-1):
            if matrix[j][i] != '*':
                print(matrix[j][i],end='')
    print()
