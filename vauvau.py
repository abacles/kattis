aa, ar, ba, br = [int(_) for _ in input().split()]
p, m, g = [int(_) for _ in input().split()]
c = 0
ans = ['none', 'one', 'both']
if 1 <= p % (aa + ar) <= aa:
    c += 1
if 1 <= p %(ba + br) <= ba:
    c += 1
print(ans[c])
c = 0
if 1 <= m % (aa + ar) <= aa:
    c += 1
if 1 <= m %(ba + br) <= ba:
    c += 1
print(ans[c])
c = 0
if 1 <= g % (aa + ar) <= aa:
    c += 1
if 1 <= g %(ba + br) <= ba:
    c += 1
print(ans[c])
