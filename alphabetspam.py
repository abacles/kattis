stuff = input()
space = ul = ll = syms = 0
for ch in stuff:
  if ch == '_':
    space += 1
  elif ord('a') <= ord(ch) <= ord('z'):
    ll += 1
  elif ord('A') <= ord(ch) <= ord('Z'):
    ul += 1
  else:
    syms += 1
print(space / len(stuff))
print(ll / len(stuff))
print(ul / len(stuff))
print(syms / len(stuff))
