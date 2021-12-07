vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

while True:
    nwords = int(input())
    if not nwords:
        break
    dvowels_max = 0
    for w in range(nwords):
        word = input()
        dvowels = 0
        for i in range(1, len(word)):
            if word[i] == word[i-1] and word[i] in vowels:
                dvowels += 1
        if dvowels > dvowels_max:
            dvowels_max = dvowels
            fav_word = word
    print(fav_word if nwords > 1 else word)
