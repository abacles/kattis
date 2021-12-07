import sys

for line in sys.stdin:
  clean = line.rstrip().lower()
  i = 0
  while i < len(clean)-2:
    if clean[i] == '0' and clean[i+1] == 'x':
      j = i+2
      while j < len(clean):
        if not ('0' <= clean[j] <= '9' or 'a' <= clean[j] <= 'f') or j-i >= 10:
          break
        j += 1
      if j > i+2:
        print(line[i:j], int(clean[i:j], 16))
        i = j
    i += 1

