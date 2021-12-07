n, k = [int(_) for _ in input().split()]
fib = [1, 1]
i = 2
while i < n:
	if fib[-1] + fib[-2] > 10e18:
		break
	fib.append(fib[-1] + fib[-2])
	i += 1
n = i - (n-i) % 2
while n > 2:
	if k <= fib[n-2-1]:
		n -= 2
	else:
		k -= fib[n-2-1]
		n -= 1
print('N' if n == 1 else 'A')
