position = int(input())
tree = {}
while True:
    branch = [int(_) for _ in input().split()]
    if branch == [-1]:
        break
    for leaf in branch[1:]:
        tree[leaf] = branch[0]

path = []
while position in tree:
    path.append(position)
    position = tree[position]
path.append(position)
print(' '.join(str(_) for _ in path))
