while True:
    counts = [int(x) for x in input().split()]
    if counts [0] == 0 and counts [1] == 0:
        break
    hsizes = []
    kheights = []
    for i in range(counts [0]):
        hsizes.append(int(input()))
    for i in range(counts [1]):
        kheights.append(int(input()))
    hsizes.sort()
    kheights.sort()
    next_knight = 0
    pay = 0
    for head in hsizes:
        while next_knight < counts [1] and kheights [next_knight] < head:
            next_knight += 1
        if next_knight >= counts [1]:
            pay = -1
            break
        pay += kheights [next_knight]
        next_knight += 1
    if pay == -1:
        print('Loowater is doomed!')
    else:
        print(pay)
