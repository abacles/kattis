for c in range(int(input())):
  n, m = [int(_) for _ in input().split()]
  beliefs = [input() for _ in range(n)]
  compromise = ['0'] * m
  for i in range(m):
    k = sum(1 for j in range(n) if beliefs[j][i] == '1')
    if k > n // 2:
      compromise[i] = '1'
  print(''.join(compromise))
