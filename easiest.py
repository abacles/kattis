while True:
    n = input()
    if n == '0':
        break
    want = sum([int(_) for _ in n])
    orig = int(n)
    p = 11
    while True:
        have = sum([int(_) for _ in str(p * orig)])
        if have == want:
            break
        p += 1
    print(p)
