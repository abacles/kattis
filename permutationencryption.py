while True:
	n, *perm = [int(_) for _ in input().split()]
	if n == 0:
		break
	msg = input()
	msg += ' ' * (n-len(msg)%n if len(msg)%n > 0 else 0)
	enc = []
	for i in range(0, len(msg), n):
		for j in range(n):
			enc.append(msg[i+perm[j]-1])
	print("\'%s\'" % ''.join(enc))
