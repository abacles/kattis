nrings = int(input())
sizes = [int(_) for _ in input().split()]

for i in range(1, nrings):
    a, b = sizes[0], sizes[i]
    # simplify a / b
    for j in range(1000, 1, -1):
        if (a%j == 0) and (b%j == 0):
            a = a // j
            b = b // j
            break
    print('%d/%d' % (a, b))
