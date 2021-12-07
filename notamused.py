import sys

day = 0
for line in sys.stdin:
    if line == 'OPEN\n':
        park = {}
        bill = {}
        day += 1
    elif line == 'CLOSE\n':
        print('Day', day)
        for name in sorted(bill.keys()):
            print('%s $%.2f' % (name, bill[name]*0.1))
        print()
    else:
        event = line.split()
        if event[0] == 'ENTER':
            park[event[1]] = int(event[2])
        else:
            bill[event[1]] = bill.get(event[1], 0) + int(event[2]) - park[event[1]]
