def mult(top,step,gap):
    if top+1<gap:
        return 1
    elif step>1:
        return top*mult(top-1,step-1,gap)
    else:
        return mult(top-1,gap,gap)

def a(m,n):
    rslt=1
    for k in range(n):
        rslt*=(m-k)
    return rslt

def c(m,n):
    return a(m,n)/a(n,n)

def select(m,n):
    if 2*n==m:
        return c(m,n)/2
    else:
        return c(m,n)

def poss(used,tot,lookup,cc):
    empty=tot-used
    rslt=cc [empty]
    for k in range(used+1,empty//2+1):
        rslt+=lookup [empty][k]
    return rslt

cities=int(input())
connected={0:1,1:1,2:1}
ccnew={2:{2:1},3:{3:8}}
for i in range(3,cities+1):
    connected [i]=(i-1)**i
    ccnew [i]={}
    for j in range(2,i//2+1):
        ccnew [i][j]=connected [j]*select(i,j)*poss(j,i,ccnew,connected)
        if 2*j<=(i-j):
            ccnew [i][j]+=mult(i-1,j,j)*(connected [i%j])
        connected [i]-=ccnew [i][j]
print(connected [cities]/(cities-1)**cities)
