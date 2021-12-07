import math
stuff = [int(_) for _ in input().split()]
print(math.ceil(stuff[0] / math.sin(math.radians(stuff[1]))))
