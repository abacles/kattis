words = input().split()
old = set()
for w in words:
    if w in old:
        print('no')
        quit()
    old.add(w)
print('yes')
