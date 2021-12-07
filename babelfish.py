import sys

translator = {}
while True:
    line = input()
    if not line: break
    eng, foreign = line.split()
    translator[foreign] = eng

for line in sys.stdin:
    line = line.strip()
    print(translator.get(line, 'eh'))
