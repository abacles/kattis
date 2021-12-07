n = int(input())
lr = tb = 0
for i in range(n):
  sword = [int(_) for _ in input()]
  tb += (1 - sword[0]) + (1 - sword[1])
  lr += (1 - sword[2]) + (1 - sword[3])
new_swords = min(tb//2, lr//2)
print(new_swords, tb - 2*new_swords, lr - 2*new_swords)
