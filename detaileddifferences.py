for _ in range(int(input())):
    a = input()
    b = input()
    print(a)
    print(b)
    for i in range(len(a)):
        if a[i] == b[i]:
            print('.', end = '')
        else:
            print('*', end = '')
    print()
    print()
