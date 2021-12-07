board = []
for i in range(8):
    board.append(list(input()))
cmd = input()

r,c = 7,0
ori = 'x'
drc = 1

for step in cmd:
    if step == 'F':
        if ori == 'x':
            c += drc
        else:
            r += drc
        if not (0 <= r < 8 and 0 <= c < 8):
            break
        if board[r][c] == 'C' or board[r][c] == 'I':
            break
    elif step == 'L':
        if ori == 'x':
            drc = -drc
            ori = 'y'
        else:
            ori = 'x'
    elif step == 'R':
        if ori == 'y':
            drc = -drc
            ori = 'x'
        else:
            ori = 'y'
    elif step == 'X':
        tr,tc = r,c
        if ori == 'x':
            tc += drc
        else:
            tr += drc
        if not (0 <= tr < 8 and 0 <= tc < 8) or board[tr][tc] != 'I':
            break
        board[tr][tc] = '.'

if board[r][c] == 'D':
    print('Diamond!')
else:
    print('Bug!')
