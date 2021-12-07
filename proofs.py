n = int(input())
proved = set()
for i in range(n):
    assumptions, conclusion = input().split('-> ')
    assumptions = assumptions.split()
    for a in assumptions:
        if a not in proved:
            print(i+1)
            quit()
    proved.add(conclusion)
print('correct')
