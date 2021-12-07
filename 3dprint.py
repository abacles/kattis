def process(sc,pc):
    if sc <= pc:
        return 1
    if pc*2 < sc:
        return 1 + process(sc,pc*2)
    return 1 + process(sc-(pc-(sc-pc)),min(pc*2,sc))

print(process(int(input()),1))
