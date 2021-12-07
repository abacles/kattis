n = int(input())

max_speed = 0

for i in range(n):
    t, d = [int(x) for x in input().split()]
    if i > 0:
        current_speed = (d - prevd) / (t - prevt)
        current_speed = int(current_speed)
        max_speed = max(max_speed, current_speed)
    prevt = t
    prevd = d

print(max_speed)
