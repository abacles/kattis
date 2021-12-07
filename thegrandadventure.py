for c in range(int(input())):
  adventure = input()
  backpack = []
  for ch in adventure:
    if ch == '.':
      continue
    elif ch == '$' or ch == '|' or ch == '*':
      backpack.append(ch)
    elif len(backpack) > 0 and (ch == 't' and backpack[-1] == '|' or ch == 'b' and backpack[-1] == '$' or ch == 'j' and backpack[-1] == '*'):
      backpack.pop()
    else:
      print('NO')
      break
  else:
    print('YES' if len(backpack) == 0 else 'NO')
