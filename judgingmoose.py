l,r = [int(_) for _ in input().split()]
if l == r and l > 0:
    print('Even',l+r)
elif l == r:
    print('Not a moose')
else:
    print('Odd',2*max(l,r))
