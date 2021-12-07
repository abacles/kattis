tot = int(input())
print(str(tot) + ':')
for f in range(1,(tot+1)//2+1):
    for s in range(f-1,f+1):
        if s > 0 and (tot % (f+s) == 0 or tot % (f+s) == f) and not (s==1 and f==1):
            print(str(f) + ',' + str(s))
