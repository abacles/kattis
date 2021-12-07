ops = ['+', '-', '*', '/']

def fourcalc(a, b, c):
    return eval(('4'+a+'4'+b+'4'+c+'4').replace('/', '//'))

def fourthought(n):
    for a in ops:
        for b in ops:
            for c in ops:
                if fourcalc(a, b, c) == n:
                    return ' '.join(['4', a, '4', b, '4', c, '4', '=', str(n)])
    return 'no solution'

for c in range(int(input())):
    n = int(input())
    print(fourthought(n))
