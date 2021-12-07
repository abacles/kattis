import math

cases = int(input())
for i in range(cases):
    enc = input()
    sl = int(math.sqrt(len(enc)))
    dec = ''
    for s in range(sl-1,-1,-1):
        for x in range(s,len(enc),sl):
            dec += enc[x]
    print(dec)
