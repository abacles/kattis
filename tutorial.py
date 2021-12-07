from math import log

def fac(n):
    if n > 12:
        return 1000000001
    if n == 1:
        return 1
    return n * fac(n-1)
def exp(n):
    if n > 29:
        return 1000000001
    if n == 1:
        return 2
    return 2 * exp(n-1)
def quadru(n):
    return n**4
def cubic(n):
    return n**3
def quadra(n):
    return n**2
def nlogn(n):
    return n * log(n,2)
def linear(n):
    return n

limit,size,atype = [int(_) for _ in input().split()]
algo = [fac,exp,quadru,cubic,quadra,nlogn,linear]

if algo[atype-1](size) <= limit:
    print('AC')
else:
    print('TLE')
