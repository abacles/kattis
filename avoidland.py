import sys

everything = [int(_) for _ in sys.stdin.read().split()]

n = everything[0]
xpawns = sorted([everything[i] for i in range(1, len(everything), 2)])
ypawns = sorted([everything[i] for i in range(2, len(everything), 2)])
moves = 0
for i in range(n):
	moves += abs(xpawns[i]-(i+1)) + abs(ypawns[i]-(i+1))
print(moves)
