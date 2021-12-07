for c in range(int(input())):
	alienx, srclang, tgtlang = input().split()
	srcval = {srclang[i]: i for i in range(len(srclang))}
	decix = 0; placeval = 1
	for i in range(len(alienx)-1, -1, -1):
		decix += srcval[alienx[i]] * placeval
		placeval *= len(srclang)
	translated_rev = []
	while decix > 0:
		translated_rev.append(tgtlang[decix % len(tgtlang)])
		decix //= len(tgtlang)
	print('Case #%d: %s' % (c+1, ''.join(reversed(translated_rev))))
