fontsample = '''
....x.xxxxx.xxxxx.x...x.xxxxx.xxxxx.xxxxx.......xxxxx.xxxxx.xxxxx
....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x
....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x
....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x.xxxxx.xxxxx.xxxxx.x...x
....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x
....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x
....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.....x.......xxxxx.xxxxx.xxxxx
'''.strip().split()

def cut(x):
	return [[x[i][j:j+5] for i in range(7)] for j in range(0, len(x[0]), 6)]
def num(flat):
	n = 0
	for i in range(0, len(flat), 35):
		n = n*10 + atoi[flat[i:i+35]]
	return n

fontbook = cut(fontsample)
plus = fontbook[7]
itoa = [10] + list(range(7)) + [8, 9]
atoi = {''.join(fontbook[itoa[i]]): i for i in range(10)}

aart = cut([input() for i in range(7)])
flatart = ''.join(''.join(aart[i]) for i in range(len(aart)))
a, b = flatart.split(''.join(plus))
c = str(num(a) + num(b))
outputs = [[] for i in range(7)]
for i in range(len(c)):
	for j in range(7):
		outputs[j].append(fontbook[itoa[int(c[i])]][j])
		if i < len(c) - 1: outputs[j].append('.');
print('\n'.join(''.join(line) for line in outputs))
