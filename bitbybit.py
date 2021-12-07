while True:
	n = int(input())
	if n == 0:
		break
	registers = [2] * 32
	for i in range(n):
		cmd, *args = input().split()
		if cmd == 'SET':
			registers[int(args[0])] = 1
		elif cmd == 'CLEAR':
			registers[int(args[0])] = 0
		else:
			a, b = [int(_) for _ in args]
			if registers[a] < 2 and registers[b] < 2:
				if cmd == 'AND':
					registers[a] = registers[a] and registers[b]
				else:
					registers[a] = registers[a] or registers[b]
			elif cmd == 'AND' and (registers[a] == 0 or registers[b] == 0):
				registers[a] = 0
			elif cmd == 'OR' and (registers[a] == 1 or registers[b] == 1):
				registers[a] = 1
			else:
				registers[a] = 2
	print(''.join(str(_) for _ in reversed(registers)).replace('2', '?'))
