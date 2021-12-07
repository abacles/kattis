def inboard(i, j):
    return 0 <= i < 5 and 0 <= j < 5

board = [input() for _ in range(5)]
nknights = 0
valid = True
for i in range(5):
    for j in range(5):
        if board[i][j] == 'k':
            nknights += 1
            for ni, nj in [(i-1, j-2), (i-2, j-1), (i-2, j+1), (i-1, j+2), (i+1, j+2), (i+2, j+1), (i+2, j-1), (i+1, j-2)]:
                if inboard(ni, nj) and board[ni][nj] == 'k':
                    valid = False
if nknights != 9:
    valid = False
print('valid' if valid else 'invalid')


