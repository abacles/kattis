nlights, roadlen = [int(_) for _ in input().split()]
time = prev = 0
for i in range(nlights):
  light = [int(_) for _ in input().split()]
  time += light[0] - prev
  prev = light[0]
  if 0 <= time % (light[1] + light[2]) < light[1]:
    time += light[1] - time % (light[1] + light[2])
time += roadlen - prev
print(time)
