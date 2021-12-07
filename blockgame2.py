def game(a, b):
    c = a % b
    if c == 0:
        return True
    banana = game(b, c)
    if banana and a == b + c:
        return False
    return True

a, b = [int(_) for _ in input().split()]
print('win' if game(max(a, b), min(a, b)) else 'lose')
