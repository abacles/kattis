days = [31,28,31,30,31,30,31,31,30,31,30,31]
week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
date = [int(_) for _ in input().split()]
tot = date[0]
for month in days[:date[1]-1]:
    tot += month
print(week[((tot-1)+3)%7])
