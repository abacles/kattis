n = int(input())
trips = {}
for i in range(n):
    place, time = input().split()
    if place in trips:
        trips[place].append(int(time))
    else:
        trips[place] = [int(time)]

for place in trips:
    trips[place].sort()

q = int(input())
for i in range(q):
    place, nth = input().split()
    print(trips[place][int(nth)-1])
