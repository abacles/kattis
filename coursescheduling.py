n = int(input())
requests = {}
for i in range(n):
    first, last, course = input().split()
    if course in requests:
        requests[course].add(first + ' ' + last)
    else:
        requests[course] = {first + ' ' + last}
        
for c in sorted(requests.keys()):
    print(c, len(requests[c]))
