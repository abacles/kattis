def shift_r(row,d):
    if d==-1:
        order=range(4)
    else:
        order=range(3,-1,-1)
    for i in order:
        for m in range(1,4):
            if i+d*m>=0 and i+d*m<4 and row [i+d*m]==0:
                row [i+d*m]=row [i+d*(m-1)]
                row [i+d*(m-1)]=0
            else:
                break
    return row


def shift_c(col,d):
    if d==-1:
        order=range(4)
    else:
        order=range(3,-1,-1)
    for i in order:
        for m in range(1,4):
            if i+d*m>=0 and i+d*m<4 and board [i+d*m][col]==0:
                board [i+d*m][col]=board [i+d*(m-1)][col]
                board [i+d*(m-1)][col]=0
            else:
                break


board=[]
for r in range(4):
    board.append([int(x) for x in input().split()])
move=int(input())
# move = {0: left, 1: up, 2: right, 3: down}
if move==0 or move==2:
    direc=move-1 # direc = {-1: left, 1: right}
    for r in range(4):
        board [r]=shift_r(board [r],direc)
        if direc==-1:
            for c in range(3):
                if board [r][c]==board [r][c+1]:
                    board [r][c]*=2
                    board [r][c+1]=0
        else:
            for c in range(3,0,-1):
                if board [r][c]==board [r][c-1]:
                    board [r][c]*=2
                    board [r][c-1]=0
        board [r]=shift_r(board [r],direc)
else:
    direc=move-2 # direc = {-1: up, 1: down}
    for c in range(4):
        shift_c(c,direc)
        if direc==-1:
            for r in range(3):
                if board [r][c]==board [r+1][c]:
                    board [r][c]*=2
                    board [r+1][c]=0
        else:
            for r in range(3,0,-1):
                if board [r][c]==board [r-1][c]:
                    board [r][c]*=2
                    board [r-1][c]=0
        shift_c(c,direc)
for line in board:
    for num in line:
        print(num,end=' ')
    print()
