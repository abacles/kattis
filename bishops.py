import sys

for line in sys.stdin:
  size = int(line.strip())
  print(size + max(0, size-2))
  
