def explore(r,c):
    dist = [[10000 for x in range(8)] for y in range(8)]
    dist[r][c] = 0
    toproc = {(r,c):'r'}
    while toproc != {}:
        proc = dict(toproc)
        toproc.clear()
        for r,c in proc:
            d = proc[(r,c)]
            if r > 0 and board[r-1][c] != 'C':
                if dist[r-1][c] > dist[r][c]+1+int(d!='u')+int(board[r-1][c]=='I'):
                    dist[r-1][c] = dist[r][c]+1+int(d!='u')+int(board[r-1][c]=='I')
                    toproc[(r-1,c)] = 'u'
            if r < 7 and board[r+1][c] != 'C':
                if dist[r+1][c] > dist[r][c]+1+int(d!='d')+int(board[r+1][c]=='I'):
                    dist[r+1][c] = dist[r][c]+1+int(d!='d')+int(board[r+1][c]=='I')
                    toproc[(r+1,c)] = 'd'
            if c > 0 and board[r][c-1] != 'C':
                if dist[r][c-1] > dist[r][c]+1+int(d!='l')+int(board[r][c-1]=='I'):
                    dist[r][c-1] = dist[r][c]+1+int(d!='l')+int(board[r][c-1]=='I')
                    toproc[(r,c-1)] = 'l'
            if c < 7 and board[r][c+1] != 'C':
                if dist[r][c+1] > dist[r][c]+1+int(d!='r')+int(board[r][c+1]=='I'):
                    dist[r][c+1] = dist[r][c]+1+int(d!='r')+int(board[r][c+1]=='I')
                    toproc[(r,c+1)] = 'r'
    return dist


def trace(er,ec,sr,sc,dist):
    if dist[er][ec] == 10000:
        print('no solution')
        return
    r,c = er,ec
    path = ''
    while not (r==sr and c==sc):
        best = (dist[r][c],r,c,None)
        if r > 0 and dist[r-1][c] < best[0]:
            best = (dist[r-1][c],r-1,c,'d')
        if r < 7 and dist[r+1][c] < best[0]:
            best = (dist[r+1][c],r+1,c,'u')
        if c > 0 and dist[r][c-1] < best[0]:
            best = (dist[r][c-1],r,c-1,'r')
        if c < 7 and dist[r][c+1] < best[0]:
            best = (dist[r][c+1],r,c+1,'l')
        path += best[3]
        if board[r][c] == 'I':
            path += 'x'
        r,c = best[1],best[2]
    path = path[::-1]
    dirtable = {'u':0,'r':1,'d':2,'l':3}
    tdir = 'r'
    readpath = ''
    ice = False
    for step in path:
        if step == 'x':
            ice = True
            continue
        if step != tdir:
            if dirtable[step] - dirtable[tdir] in [1,-3]:
                readpath += 'R'
            else:
                readpath += 'L'
            tdir = step
        if ice:
            readpath += 'X'
            ice = False
        readpath += 'F'
    print(readpath)
    return
            
                
board = []
for i in range(8):
    board.extend(input().split())

disttable = explore(7,0)
for r in range(8):
    if 'D' in board[r]:
        trace(r,board[r].index('D'),7,0,disttable)
        break
