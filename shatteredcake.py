import sys

everything = sys.stdin.read().split()

area = 0
for i in range(2, len(everything), 2):
    area += int(everything[i]) * int(everything[i+1])
print(area // int(everything[0]))
