empty, found, trade = [int(_) for _ in input().split()]
soda = (empty + found) // trade
bottles = (empty + found) % trade + soda
while bottles >= trade:
    xchange, bottles = divmod(bottles, trade)
    soda += xchange
    bottles += xchange
print(soda)
