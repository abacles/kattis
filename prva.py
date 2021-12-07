r, c = [int(_) for _ in input().split()]
crossword = [input() for _ in range(r)]

smallest = 'z' * 20
for dx, dy in [(1, 0), (0, 1)]:
    for x in range(c):
        ox = x
        for y in range(r):
            if ((dx and x-dx >= 0 and crossword[y][x-dx] != '#') or
                (dy and y-dy >= 0 and crossword[y-dy][x] != '#')):
                continue
            word = []
            while x < c and y < r and crossword[y][x] != '#':
                word.append(crossword[y][x])
                x, y = x+dx, y+dy
            word = ''.join(word)
            if len(word) >= 2 and word < smallest:
                smallest = ''.join(word)
            x = ox
print(smallest)
