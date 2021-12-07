from collections import deque

r,c = [int(_) for _ in input().split()]
board = []
for i in range(r):
    board.append(list(input()))
for j in range(c):
    avai = deque()
    for i in range(r-1,-1,-1):
        if board[i][j] == 'a' and len(avai) > 0:
            a = avai.popleft()
            board[i][j],board[a][j] = board[a][j],board[i][j]
        if board[i][j] == '.':
            avai.append(i)
        elif board[i][j] == '#':
            avai.clear()
for row in board:
    print(''.join(row))
