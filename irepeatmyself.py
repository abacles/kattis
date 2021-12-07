for c in range(int(input())):
    seq = input()
    for i in range(len(seq)):
        prefix = seq[:i+1]
        repeat = len(seq)//(i+1) + 1
        if (prefix*repeat).startswith(seq):
            break
    print(i+1)
