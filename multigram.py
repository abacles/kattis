gram = input()
freq = [[0]*26]
for ch in gram:
    freq.append(freq[-1][:])
    freq[-1][ord(ch)-ord('a')] += 1

for size in range(1, len(gram)//2+1):
    if len(gram) % size:
        continue
    satisfy = True
    for i in range(2*size, len(gram)+1, size):
        for j in range(26):
            if freq[i][j] != freq[size][j]*(i//size):
                satisfy = False
                break
        if not satisfy:
            break
    if satisfy:
        print(gram[:size])
        break
else:
    print(-1)
