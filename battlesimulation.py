counters = {'R': 'S', 'B': 'K', 'L': 'H'}
code = {'R': 1, 'B': 2, 'L': 4}
monster = input()
mech = []
i = cc = 0
while i+2 < len(monster):
	if cc == 0:
		cc = code[monster[i]] + code[monster[i+1]]
	cc += code[monster[i+2]]
	if cc == 7:
		mech.append('C')
		i += 3
		cc = 0
	else:
		mech.append(counters[monster[i]])
		cc -= code[monster[i]]
		i += 1
while i < len(monster):
	mech.append(counters[monster[i]])
	i += 1
print(''.join(mech))
