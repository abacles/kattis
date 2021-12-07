cost,total = float(input()),0
for i in range(int(input())):
    lawn = [float(_) for _ in input().split()]
    total += cost * lawn[0] * lawn[1]
print(total)
