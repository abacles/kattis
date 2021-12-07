ncomm, price = [int(_) for _ in input().split()]
profits = [int(_)-price for _ in input().split()]
maxsum = csum = profits[0]
for i in range(1, ncomm):
    csum += profits[i]
    if profits[i] > csum:
        csum = profits[i]
    if csum > maxsum:
        maxsum = csum
print(maxsum)
