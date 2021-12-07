msg = input()
bestlen = len(msg)
for i in range(len(msg)):
    for j in range(i+2, len(msg)):
        c = msg.count(msg[i:j])
        if len(msg)-c*(j-i)+c+(j-i) < bestlen:
            bestlen = len(msg)-c*(j-i)+c+(j-i)
print(bestlen)
