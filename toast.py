import math

data = [int(x) for x in raw_input().split()]
people,arm,toasts = data [0],data [1],data [2]

reached = toasts*2 / people
furthest = (360/people) * reached / 2
high = arm / math.sin(math.radians(furthest/2))

if reached == people:
    low = arm
else:
    nearest = (360/people) * (reached/2 + 1)
    

print(str(arm) + ' ' + str(high))
