def shrink(topleft, botright, k, dim):
    if k == '0':
        newtopleft = topleft
    elif k == '1':
        newtopleft = [(topleft[0]+botright[0])//2+1, topleft[1]]
    elif k == '2':
        newtopleft = [topleft[0], (topleft[1]+botright[1])//2+1]
    elif k == '3':
        newtopleft = [(topleft[0]+botright[0])//2+1, (topleft[1]+botright[1])//2+1]
    return newtopleft, [newtopleft[0]+dim-1, newtopleft[1]+dim-1]

quadkey = input()
dim = int((4 ** (len(quadkey))) ** 0.5)
topleft = [0, 0]; botright = [dim-1, dim-1]
for k in quadkey:
    dim //= 2
    topleft, botright = shrink(topleft, botright, k, dim)
print(len(quadkey), topleft[0], topleft[1])
