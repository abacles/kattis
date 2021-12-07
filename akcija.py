books = int(input())
prices = []
for i in range(books):
    prices.append(int(input()))
prices.sort()
prices = [0,0] + prices

pay = 0
for i in range(books+1,1,-3):
    group = (prices[i],prices[i-1],prices[i-2])
    pay += sum(group) - min(group)

print(pay)
