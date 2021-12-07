import sys

inf=sys.stdin.read()
words = []
for line in inf.split('\n'):
    words.extend(line.split())

prev = set()
for i in range(len(words)):
    for j in range(len(words)):
        if i != j and not str(words[i])+str(words[j]) in prev:
            prev.add(str(words[i])+str(words[j]))

s = sorted(list(prev))
for x in s:
    print(x)
