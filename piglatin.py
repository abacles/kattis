import sys

vowels = set(['a','e','i','o','u','y'])

for line in sys.stdin:
  eng = line.strip()
  latin = []
  for word in eng.split():
    if word[0] in vowels:
      latin.append(word + 'yay')
    else:
      for i in range(len(word)):
        if word[i] in vowels:
          break
      latin.append(word[i:] + word[:i] + 'ay')
  print(' '.join(latin))
