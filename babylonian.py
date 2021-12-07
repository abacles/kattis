for c in range(int(input())):
    digits = [int(_) if _ else 0 for _ in input().split(',')]
    print(sum(digits[i]*60**(len(digits)-i-1) for i in range(len(digits))))
