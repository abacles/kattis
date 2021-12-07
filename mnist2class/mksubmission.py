with open('weights.txt') as fin:
    w = [line.split() for line in fin]

with open('mnist2class.py', 'w') as fout:
    fout.write('w = ')
    print(w, file = fout)
    fout.write('\n')
    fout.write('for j in range(30):\n')
    fout.write('\tfor i in range(51):\n')
    fout.write('\t\tprint(w[i][j], end = " " if i < 50 else "\\n")\n')
