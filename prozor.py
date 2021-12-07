def count(i_init, j_init, dim, a):
  '''
    returns the number of flies in the block with its top-left corner at (i_init, j_init) and with side length dim
  '''
  c = 0
  for i in range(i_init+1, i_init+dim-1):
    for j in range(j_init+1, j_init+dim-1):
      if a[i][j] == '*':
        c += 1
  return c

nrows, ncols, rsize = [int(_) for _ in input().split()]
window = [input() for _ in range(nrows)]

maxhit = 0

for i in range(nrows-rsize+1):
  for j in range(ncols-rsize+1):
    this_hit = count(i, j, rsize, window)
    if this_hit > maxhit:
      maxhit = this_hit
      hitpos = (i, j)

type2symbol = {3: '+', 2: '|', 1: '-'}
print(maxhit)
for i in range(nrows):
  for j in range(ncols):
    type = 0
    if (hitpos[0] <= i < hitpos[0]+rsize and
        hitpos[1] <= j < hitpos[1]+rsize):
      if i == hitpos[0] or i == hitpos[0]+rsize-1:
        type += 1
      if j == hitpos[1] or j == hitpos[1]+rsize-1:
        type += 2
    if type == 0: # normal
      print(window[i][j], end = '')
    else: # border or corner
      print(type2symbol[type], end = '')
  print()
