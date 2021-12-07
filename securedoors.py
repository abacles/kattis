people = set()
for i in range(int(input())):
    event = input().split()
    if event[0] == 'entry':
        if event[1] not in people:
            print(event[1], 'entered')
            people.add(event[1])
        else:
            print(event[1], 'entered (ANOMALY)')
    else:
        if event[1] in people:
            print(event[1], 'exited')
            people.remove(event[1])
        else:
            print(event[1], 'exited (ANOMALY)')
