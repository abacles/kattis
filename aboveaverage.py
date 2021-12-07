ncases = int(input())
for _ in range(ncases):
    grades = [int(_) for _ in input().split()][1:]
    avg = sum(grades) / len(grades)
    print('%.3f%%' % round(sum([1 if g > avg else 0 for g in grades]) / len(grades) * 100, 3))
