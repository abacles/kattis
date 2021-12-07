n = int(input())
lang = input().split()
recents = {}
awkwardness = n
for i in range(n):
    if lang[i] in recents:
        awkwardness = min(awkwardness, i - recents[lang[i]])
    recents[lang[i]] = i
print(awkwardness)
