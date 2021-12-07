def gcf(a, b):
    if not a:
        return b
    return gcf(b % a, a)

temp = [int(_) for _ in input().split('/')]
temp[0] -= 32 * temp[1]
temp[1] *= 9
temp[0] *= 5
f = gcf(temp[0], temp[1])
temp[0] //= f
temp[1] //= f
if temp[1] < 0:
    temp[1] *= -1
    temp[0] *= -1
print(str(temp[0]) + '/' + str(temp[1]))
