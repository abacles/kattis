import sys
import math

raw = sys.stdin.read()

for line in raw.split('\n'):
    if line == '':
        break
    n = int(line)
    fsum = 1
    limit = int(math.ceil(math.sqrt(n)))
    for i in range(2,limit):
        if n%i == 0:
            fsum += i+n/i
    if limit**2 == n:
        fsum += math.sqrt(n)
    if fsum == n:
        print(line + ' perfect')
    elif fsum >= n-2 and fsum <= n+2:
        print(line + ' almost perfect')
    else:
        print(line + ' not perfect')
