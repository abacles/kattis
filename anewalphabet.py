nd_raw = "a@ b8 c( d|) e3 f# g6 h[-] i| j_| k|< l1 m[]\/[] n[]\[] o0 p|D q(,) r|Z s$ t'][' u|_| v\/ w\/\/ x}{ y`/ z2"
newdict = {}
for sub in nd_raw.split():
    newdict[sub[0]] = sub[1:]
msg = input().lower()
nmsg = ''
for ch in msg:
    nmsg += newdict.get(ch, ch)
print(nmsg)
