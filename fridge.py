letters = [[0, i] for i in range(10)]
for l in input():
	letters[ord(l)-ord('0')][0] += 1
letters.sort()

if letters[0][1] != 0:
	print(str(letters[0][1]) * (letters[0][0]+1))
elif letters[0][0] == letters[1][0]:
	print(str(letters[1][1]) * (letters[1][0]+1))
else:
	prefix = min(i for i in range(1, 10) if letters[i][0] > 0)
	print(str(prefix) + '0' * (letters[0][0]+1))
