have = int(input())
months = int(input())
print(have * (months+1) - sum([int(input()) for _ in range(months)]))
