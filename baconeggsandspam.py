while True:
    n = int(input())
    if n == 0:
        break
    orders = {}
    for i in range(n):
        stuff = input().split()
        for dish in stuff[1:]:
            if dish in orders:
                orders[dish].append(stuff[0])
            else:
                orders[dish] = [stuff[0]]
    for dish in sorted(orders.keys()):
        print(dish, ' '.join(sorted(orders[dish])))
    print()
