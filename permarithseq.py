def arith(s):
    for i in range(2,len(s)):
        if s[i]-s[i-1] != s[i-1]-s[i-2]:
            return False
    return True

cases = int(input())

for i in range(cases):
    seq = [int(_) for _ in input().split()]
    if arith(seq[1:]):
        print('arithmetic')
    elif arith(sorted(seq[1:])):
        print('permuted arithmetic')
    else:
        print('non-arithmetic')
