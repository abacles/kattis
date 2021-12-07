def lchild(n):
    return n*2 + 1
def rchild(n):
    return n*2 + 2

raw = input().strip()
if ' ' in raw:
    depth,trav = raw.split()
    depth = int(depth)
else:
    depth = int(raw)
    trav = ''

root = 2**(depth+1) - 1
get = {'L':lchild,'R':rchild}

pos = 0
for step in trav:
    pos = get[step](pos)

print(root - pos)
