days=int(input())
prices=[]
for i in range(days):
    prices.append(int(input()))
money=100
shares=0
i=0
for p in prices:
    if i<len(prices)-1:
        if p>prices [i+1]:
            money+=shares*p
            shares=0
        else:
            if shares+money//p<=100000:
                shares+=money//p
                money%=p
            else:
                buy=100000-shares
                shares=100000
                money-=buy*p
    else:
        money+=shares*p
        shares=0
    i+=1
print(money)
