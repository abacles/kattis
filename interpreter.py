import sys

def dn2(d, n):
    register[d] = n
def dn3(d, n):
    register[d] = (register[d] + n) % 1000
def dn4(d, n):
    register[d] = (register[d] * n) % 1000
def ds5(d, s):
    register[d] = register[s]
def ds6(d, s):
    register[d] = (register[d] + register[s]) % 1000
def ds7(d, s):
    register[d] = (register[d] * register[s]) % 1000
def da8(d, a):
    register[d] = int(ram[register[a]])
def sa9(s, a):
    ram[register[a]] = '0'*(3-len(str(register[s]))) + str(register[s])

ram = ['000'] * 1000
register = [0] * 10
for i, line in enumerate(sys.stdin):
    ram[i] = line.strip()

f = [0, 0, dn2, dn3, dn4, ds5, ds6, ds7, da8, sa9]
step = 0
totstep = 0
while True:
    i = ram[step]
    if i[0] == '1':
        break
    if i[0] == '0':
        step = register[int(i[1])] if register[int(i[2])] != 0 else step + 1
    else:
        f[int(i[0])](int(i[1]), int(i[2]))
        step += 1
    totstep += 1
print(totstep + 1)
