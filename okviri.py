def stamp(p, i, ch):
    p[0][i+2] = p[-1][i+2] = p[1][i+1] = p[1][i+3] = p[-2][i+1] = p[-2][i+3] = p[2][i] = p[2][i+4] = ch

text = input()
pattern = [['.']*(1+4*len(text)) for _ in range(5)]
for i in range(len(text)):
    stamp(pattern, i*4, '#')
    pattern[2][i*4+2] = text[i]
for i in range(2, len(text), 3):
    stamp(pattern, i*4, '*')
    
for line in pattern:
    print(''.join(line))
