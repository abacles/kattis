import itertools

for c in range(int(input())):
    nums = [int(_) for _ in input().split()][1:]
    print('Case #' + str(c+1) + ':')
    ps = {}
    found = False
    for s in itertools.product([True, False], repeat = 20):
        ssum = 0
        for i in range(20):
            if s[i]:
                ssum += nums[i]
        if ssum in ps:
            subset = []
            for i in range(20):
                if s[i]:
                    subset.append(str(nums[i]))
            print(' '.join(subset))
            subset = []
            for i in range(20):
                if ps[ssum][i]:
                    subset.append(str(nums[i]))
            print(' '.join(subset))
            found = True
            break
        ps[ssum] = s
    if not found:
        print('Impossible')
