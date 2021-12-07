s = input()
add2back = [26 for _ in range(len(s))]
minletters = 26
for i in range(len(s)-1, -1, -1):
	add2back[i] = ord('z') - ord(s[i])
	for j in range(i+1, len(s)):
		if s[j] > s[i] and (ord(s[j])-ord(s[i])-1+add2back[j]) < add2back[i]:
			add2back[i] = ord(s[j])-ord(s[i])-1+add2back[j]
	minletters = min(minletters, add2back[i] + ord(s[i]) - ord('a'))
print(minletters)
