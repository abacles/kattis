import sys

totdist = 0
prevtime = 0
speed = 0
for line in sys.stdin:
	line = line.split()
	time = line[0].split(':')
	time = int(time[0])*3600 + int(time[1])*60 + int(time[2])
	totdist += (time - prevtime) / 3600 * speed
	if len(line) == 2:
		speed = int(line[1])
	else:
		print('%s %.2f km' % (line[0], totdist))
	prevtime = time
