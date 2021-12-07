while True:
    a, b = [int(_) for _ in input().split()]
    if not a and not b:
        break
    if a + b == 13:
        print('Never speak again.')
    elif a < b:
        print('Left beehind.')
    elif a > b:
        print('To the convention.')
    else:
        print('Undecided.')
