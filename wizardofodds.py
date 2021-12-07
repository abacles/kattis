secret,qs = [int(_) for _ in input().split()]
if secret <= 2**qs:
    print('Your wish is granted!')
else:
    print('You will become a flying monkey!')
