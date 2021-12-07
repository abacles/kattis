shift = int(input())
msg = [ord(_)-ord('a') for _ in input()]
nsteps = int(input())
goodshifts = 0
bad = [ord(_)-ord('a') for _ in 'aeiouy']
for i in range(nsteps):
	vowels = 0
	for j in range(len(msg)):
		msg[j] = (msg[j] + shift) % 26
		if msg[j] in bad:
			vowels += 1
	if 2 * vowels < (len(msg) - vowels):
		goodshifts += 1
print('Boris' if goodshifts > (nsteps-goodshifts) else 'Colleague')
