matches = input()
stars,rank,conseq = 0,25,0
sreq = [0] + [5]*10 + [4]*5 + [3]*5 + [2]*5
for m in matches:
    if m == 'W':
        stars += 1
        conseq += 1
        if conseq >= 3 and 6 <= rank <= 25:
            stars += 1
        if stars > sreq[rank]:
            stars -= sreq[rank]
            rank -= 1
            if rank == 0:
                break
    else:
        conseq = 0
        if rank <= 20:
            stars -= 1
            if rank < 20 and stars < 0:
                rank += 1
                stars = sreq[rank] - 1
            elif rank == 20 and stars < 0:
                stars = 0
if rank == 0:
    print('Legend')
else:
    print(rank)
