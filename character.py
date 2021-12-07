def fac(n):
    if n <= 1:
        return 1
    return n * fac(n-1)

p = int(input())
tot = 0
for i in range(2, p+1):
    tot += fac(p) // (fac(i) * fac(p - i))

print(tot)
