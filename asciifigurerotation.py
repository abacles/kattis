first = True
while True:
	n = int(input())
	if n == 0: break;
	if first: first = False;
	else: print();
	figure = [list(input()) for i in range(n)]
	width = max(len(figure[i]) for i in range(n))
	for i in range(n):
		figure[i] += [' '] * (width-len(figure[i]))
	for j in range(width):
		line = ''.join(figure[i][j] for i in range(n))
		line = line.replace('|', '$')
		line = line.replace('-', '|')
		line = line.replace('$', '-')
		print(line[::-1].rstrip())
