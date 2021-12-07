n = int(input())
while True:
    s = 0
    for ch in str(n):
        s += ord(ch) - ord('0')
    if n % s == 0:
        break
    n += 1
print(n)
