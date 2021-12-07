def strsign(s):
    return 1 if float(s) > 0 else -1

with open('weights4.txt') as fin:
    w = [[strsign(_) for _ in line.split()] for line in fin]

with open('mnist10class.py', 'w') as fout:
    fout.write('w = ')
    print(w, file = fout)
    fout.write('\n')
    fout.write('for j in range(150):\n')
    fout.write('\tfor i in range(51):\n')
    fout.write('\t\tprint(w[i][j], end = " " if i < 50 else "\\n")\n')
