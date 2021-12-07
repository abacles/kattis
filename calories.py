calindex = [9, 4, 4, 4, 7]
while True:
    totcal = fatcal = 0
    while True:
        line = input()
        if line == '-':
            break
        stats = line.split()
        percent = cal = 0
        for i in range(5):
            if stats[i][-1] == 'g':
                stats[i] = int(stats[i][:-1]) * calindex[i]
                cal += stats[i]
            elif stats[i][-1] == 'C':
                stats[i] = int(stats[i][:-1])
                cal += stats[i]
            else:
                percent += int(stats[i][:-1])
        cal = cal * (100 / (100-percent))
        if type(stats[0]) is str:
            stats[0] = cal * int(stats[0][:-1]) / 100
        totcal += cal
        fatcal += stats[0]
    if totcal == fatcal == 0:
        break
    print('%.0f%%' % (fatcal/totcal*100))
